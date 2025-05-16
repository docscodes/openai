import os
import openai
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

try:
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        max_tokens=100,
        messages=[{'role': 'user', 'content': 'What is OpenAI?'}])
except openai.AuthenticationError as e:
    print(f"Authentication Error: {e}")
except openai.InvalidRequestError as e:
    print(f"Invalid Request Error: {e}")
except openai.APIError as e:
    print(f"API Error: {e}")
except openai.APIConnectionError as e:
    print(f"API Connection Error: {e}")
except openai.Timeout as e:
    print(f"Timeout Error: {e}")
except openai.ServiceUnavailableError as e:
    print(f"Service Unavailable Error: {e}")
except openai.RateLimitError as e:
    print(f"Rate Limit Error: {e}")
