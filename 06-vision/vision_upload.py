import os
import base64
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_path = "sample.jpeg"
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {"type": "image_url", "image_url": {
                "url": f"data:image/jpeg;base64, {base64_image}", 
            }},
        ],
    }])

print(response)
print(type(response))
print(response.model)
print(response.choices[0].message.content)
