import os
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

response = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {"type": "image_url", "image_url": {
                "url": "https://images.unsplash.com/photo-1597431783670-205a592f954e?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=800&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTcwMzE3ODc4Ng&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1900"
            }},
        ],
    }])

print(response)
print(type(response))
print(response.model)
print(response.choices[0].message.content)
