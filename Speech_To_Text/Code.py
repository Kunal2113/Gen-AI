import openai

openai.api_key = "your api key "

from openai import OpenAI
client = OpenAI(api_key=openai.api_key)

audio_file =open("/content/output.mp3","rb")


response = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)
print(response)
