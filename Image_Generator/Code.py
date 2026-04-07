pip install config

import openai

openai.api_key="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"

from openai import OpenAI
client = OpenAI(api_key=openai.api_key)

import openai
from openai import OpenAI
client = OpenAI(api_key=openai.api_key)

response = client.images.generate(
    model="dall-e-2",
    prompt="a white siamese cat",
    size="1024x1024",
    n=1

)
print(response.data[0].url)
