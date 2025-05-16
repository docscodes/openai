import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=100,
    temperature=0.5,
    messages=[{'role': 'user', 'content': 'Complete the following proverb.dont make a mountain'}])

print(response.choices[0].message.content)
