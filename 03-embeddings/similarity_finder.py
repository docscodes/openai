import numpy as np
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

response = client.embeddings.create(
    input=["you are good", "you are awesome"],
    model="text-embedding-ada-002")

embedding_1 = response.data[0].embedding
embedding_2 = response.data[1].embedding

similarity_score = np.dot(embedding_1, embedding_2)
print(similarity_score*100, "%")
