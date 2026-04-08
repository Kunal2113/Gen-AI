pip install config

import openai

openai.api_key = "your api key "

from openai import OpenAI
client = OpenAI(api_key=openai.api_key)

responce =client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="My name is kunal rathore from hindustan college of science and technology CSE branch section B"
)
responce.stream_to_file("output.mp3")
