from groq import Groq

# Read the API key from api_key.txt
with open("api_key.txt", "r") as file:
    api_key = file.read().strip()

client = Groq(api_key=api_key)
completion = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=[
        {
            "role": "system",
            "content": "you are a content moderator, and you will moderate this conversation, your answers will be no longer than 20 words.",
        },
        {
            "role": "user",
            "content": "Hi please assist in creating a najana account.",
        }
    ],
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
