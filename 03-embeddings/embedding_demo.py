import os
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

response = client.embeddings.create(
    input="learn share and grow",
    model="text-embedding-ada-002")

print(response)
print(response.data[0].embedding)
