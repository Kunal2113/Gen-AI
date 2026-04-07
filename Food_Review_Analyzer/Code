pip install openAI
import openai
openai.api_key = "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"
messages=[
    {"role":"system", "content":'''You are a precise Sentiment Analysis Assistant for food delivery reviews Your task is to classify user reviews into one of three categories
    1. GOOD: Positive feedback regarding food quality, taste, or delivery speed.
        2. OKAY: Mixed reviews, average experiences, or minor complaints that don't ruin the meal.
        3. BAD: Negative feedback regarding cold food, missing items, poor hygiene, or extreme delays.'''},

    {"role": "user", "content": "The ambience of the restaurant was good but the food was pathetic which spoiled my whole experience"},
    {"role": "user", "content": "The food and the place was amazing will definitely came here next time!!"},
    {"role": "user", "content": "The paneer dish was neither too good nor to bad. It's a one time exoperience."}

]
chat_response = openai.chat.completions.create(
    model = "gpt-5-nano",
    messages = messages
)
  
chat_response.choices[0].message.content
