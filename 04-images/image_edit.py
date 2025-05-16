import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.images.generate(
    prompt="A big house with a tube in the swimming pool",
    image=open("housewithpool.png", mode="rb"),
    mask=open("masked.png", mode="rb"),
    n=1,
    size="1024x1024")

print(response)
