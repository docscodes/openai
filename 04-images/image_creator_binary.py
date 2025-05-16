import os
from openai import OpenAI
from base64 import b64decode

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.images.generate(
    prompt="Ferrari in himalayas",
    n=1,
    size="1024x1024",
    response_format="b64_json")

img_bytes = b64decode(response.data[0].b64_json)
img_file = open("ferrari.png", "wb")
img_file.write(img_bytes)
img_file.close()
