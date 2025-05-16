import numpy as np
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

text = ["I am playing video games", "I am coding",
        "I am angry", "I am going to movies."]

response = client.embeddings.create(
    input=text,
    model="text-embedding-ada-002")

for i in range(len(text) - 1):
    for j in range(i + 1, len(text)):
        embedding_1 = response.data[i].embedding
        embedding_2 = response.data[j].embedding

        similarity_score = np.dot(embedding_1, embedding_2)
        print("text similarity for ", text[i], " and ", text[j])
        print(similarity_score*100, "%")
