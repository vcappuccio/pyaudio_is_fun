# Transcribes speech input from the microphone to text until "stop" is said.

This Python script leverages the SpeechRecognition library to seamlessly integrate speech recognition capabilities into your applications. It continuously listens for speech input from a microphone, transcribes the speech using Google Speech Recognition, and appends each utterance to a list. The script is designed to stop listening when the word "stop" is detected in the last utterance, providing a user-friendly way to control the listening process.

## Features

- **Automatic Microphone Detection**: The script automatically identifies and selects a suitable microphone device for speech recognition.
- **Continuous Speech Listening**: It listens for speech input in real-time, ensuring that no speech is missed.
- **Speech Transcription**: Utilizes Google Speech Recognition to transcribe speech into text, providing accurate and reliable transcriptions.
- **Dynamic Utterance Collection**: Appends each recognized utterance to a list, allowing for easy storage and processing of the transcribed speech.
- **User-Controlled Listening**: Stops listening when the user says "stop", offering a convenient way to control the listening process.
- **Error Handling and Logging**: Gracefully handles exceptions and logs errors, ensuring smooth operation and easy debugging.

## Requirements

- **Python 3.x**: The script is compatible with Python 3.x versions.
- **SpeechRecognition Library**: This library is essential for speech recognition capabilities.
- **PyAudio Library**: Required for accessing the microphone and capturing audio input.

## Installation

To get started with this script, follow these steps:

1. **Clone the Repository or Download the Script**: You can either clone the repository to your local machine or download the script directly.

2. **Install the Required Libraries**: Before running the script, ensure that you have the necessary libraries installed. You can install them using pip:


