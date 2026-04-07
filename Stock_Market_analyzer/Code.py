from google.colab import drive

drive.mount('/content/drive',force_remount=True)

file_path= '/content/drive/MyDrive/Stock_Market/Asian_paints.txt'

with open(file_path, 'r')as file:
  content = file.read()

base_instruction='''You are a helpful assistant which helps  financial analysts retrieve the relevant financial information
and business related information from the documents I provide as input.
Give below are some questions and the transcripts of an earning call of a paints company, Asian Paints which was
attended by the top managementof the firm.
Try to respond with specific numbers and facts wherever it is possible.
If you are unsure about any of the question given to you simply say that you dont know about that.'''


question  = "Which company did asian paint accquire"

prompt = base_instruction+"\n\n"+"Question{0}".format(question)+"\n\n"+"Transcript:\n{0}".format(content)

print(prompt)

messages = [{
    "role": "system",
    "content": prompt
}]

pip install openAI

import openai

openai.api_key = "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"

chat_response = openai.chat.completions.create(
    model = "gpt-3.5-turbo-16k",
    messages=messages,
    max_tokens=1000,
    temperature=0.5,
    n=1,
    stop = None,
    frequency_penalty=0,
    presence_penalty=0,

)
print(chat_response.choices[0].message.content)
