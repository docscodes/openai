import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

audio_file = open("sample_french.mp3", "rb")

response = client.audio.translate(
    model="whisper-1",
    file=audio_file)

print(response)
