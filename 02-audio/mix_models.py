import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


audio_file = open("aws_lambda.mp3", "rb")

response = client.audio.translate(
    model="whisper-1",
    file=audio_file)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{'role': 'user', 'content': 'Summarize the text in to 5 bullet points:'+response.text}])

print(response)
