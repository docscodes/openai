import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.images.generate(
    prompt="Programmer on the moon",
    n=3,
    size="1024x1024")

print(response)
