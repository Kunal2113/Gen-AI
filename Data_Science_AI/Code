pip install openAI
import openai
openai.api_key = "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"
messages=[
    {"role":"system", "content":'''You are an ai assistant that will answer only the questions related to data science in brief . If any user asks a  random question , you simply have to respond that “sorry! I can’t answer this question “, I can answer only data science related stuff.'''},

    {"role": "user", "content": "what is Machine Learning"},
    {"role": "user", "content": "what is the capital of india"},

]
chat_response = openai.chat.completions.create(
    model = "gpt-5-nano",
    messages = messages
)
chat_response.choices[0].message.content
