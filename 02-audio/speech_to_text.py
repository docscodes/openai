import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

audio_file = open("sample_english.m4a", "rb")

response = client.audio.transcribe(
    model="whisper-1",
    file=audio_file,
    language="en",
    response_format="text")

print(response)
