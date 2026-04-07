from google.colab import drive

drive.mount('/content/drive',force_remount=True)

file_path= '/content/drive/MyDrive/Stock_Market/Hindustan-College-of-Science-Technology20260227-1.txt'

with open(file_path, 'r')as file:

  content = file.read()

len(content)


base_instruction='''You are a helpful assistant which help scan the complete document and answer the question according to the analysis retrieve the relevant information from the documents I provide as input.
Give below are some questions , Hindustan College Of Science and Technology which was
a very good college.
Try to respond with specific numbers and facts wherever it is possible.
If any information which is asked is not present, kindly say 'I don't know doesn't give any random information.
**Don't miss any information from the document give the correct response as possible**'''


questions = [
    "The doc shared is of which year?",
    "No. Of students enrolled in the session 2025-26, Give me detailed breakdown.",
    "Is there a % increase in no. of students enrolled in consecutive years or not, Give the complete comphrehensive calculation. If data is not provided in the text file just say i dont have data",
    "Give me the complete faculty details who has the designation as 'professor'.",
    "No of total B.tech students, M.tech students, phd holders across all years.",
    "Give me the detail breakdown of fee details for B.tech."
]


questions_text = "\n".join([f"{i+1}. {q}" for i, q in enumerate(questions)])


prompt = f"{base_instruction}\n\nQUESTIONS:\n{questions_text}\n\nTRANSCRIPT:\n{content}"


messages = [{
    "role": "system","content": prompt
}]


pip install openAI

import openai

openai.api_key = "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"

chat_response = openai.chat.completions.create(
    model = "gpt-3.5-turbo-16k",
    messages=messages,
    max_tokens=1000,
    temperature=0.2,
    n=1,
    stop = None,
    frequency_penalty=0,
    presence_penalty=0,

)
print(chat_response.choices[0].message.content)
