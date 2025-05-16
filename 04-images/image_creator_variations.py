import os
from openai import OpenAI
from base64 import b64decode

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.images.generate(
    image=open("ferrari.png", mode="rb"),
    n=2,
    size="256x256")

print(response)
