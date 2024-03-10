
import speech_recognition as sr
import logging
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1236/v1", api_key="not-needed")

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def find_microphone():
    """Find the microphone device index."""
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "Chill" in name: 
            logging.info(f"Found microphone: {name} at index {index}")
            return index
    logging.error("No suitable microphone found.")
    return None

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# List to store recognized speech
recognized_speech = []

# Find the microphone
device_index = find_microphone()
if device_index is None:
    logging.error("Exiting due to no suitable microphone found.")
    exit(1)

"""
Continuously listen for speech input from the microphone. 

Transcribe the speech using Google Speech Recognition and append each 
utterance to the recognized_speech list. 

Check for "stop" in the last utterance to determine when to stop listening.

Handle any exceptions from the speech recognition library and log errors.
"""
"""
Continuously listen for speech input from the microphone. Recognize the speech using 
Google Speech Recognition and append each utterance to the recognized_speech list.
Check for "stop" in the last utterance to break out of the loop.
"""
"""
Continuously listen for speech input from the microphone. 

Transcribe the speech using Google Speech Recognition and append each 
utterance to the recognized_speech list. 

Check for "stop" in the last utterance to determine when to stop listening.

Handle any exceptions from the speech recognition library and log errors.
"""
while True:
    try:
        # Specified microphone:
        with sr.Microphone(device_index=device_index) as source:
            print("Listening...")
            
            audio = r.listen(source)#, timeout=5, phrase_time_limit=10)
            # phrase_time_limit is the number of seconds to listen for a phrase before it interrupts the listening.
            # timeout is the number of seconds to wait before interrupting the listening.

        # Recognize speech
        text = r.recognize_google(audio)
        print("You said: " + text)

        recognized_speech.append(text)

        messages = [
            {"role": "system", "content": "You are a friendly and helpful assistant, and you will moderate this conversation."},
                 ]
        for speech in recognized_speech:
            messages.append({"role": "user", "content": speech})

        completion = client.chat.completions.create(
            model="local-model",  # choose your model
            messages=messages,
            temperature=0.2, # Faster computer? or Groq?
            # Append the recognized speech to the list
            # recognized_speech.append(text)
            # Chroma-DB?
        )
    except sr.UnknownValueError:
        logging.error("Recognition could not understand audio")
    except sr.RequestError as e:
        logging.error(f"Could not request results: {e}")
    except Exception as e:
        logging.exception("An unexpected error occurred: %s", e)

    # Say stop.
    if recognized_speech and "stop" in recognized_speech[-1].lower():
        break

# or Vector-DB?
#with open('recognized_speech.txt', 'w') as f:
#    for speech in recognized_speech:
#        f.write("%s\n" % speech)

print("Finished listening.")
