import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.moderations.create(
    model='text-moderation-latest',
    # input='My favorite movie is kill bill'
    input='I hate myself and want to harm myself'
)

print(response)
print(response.results[0].flagged)
print(response.results[0].categories)
print(response.results[0].category_scores)
print(response.results[0].categories.self_harm)
print(response.results[0].category_scores.self_harm)
