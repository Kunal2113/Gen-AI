pip install openAI

import openai

openai.api_key = "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"

messages=[
    {
        "role": "system",
        "content": """You are a Strategic Academic Advisor for B.Tech students.Your goal is to create high-efficiency, distraction-free timetables that balance: 1. Core Subjects (Academic Excellence),2. Technical Workshops (Skill Building),3. Placement Training (Aptitude & Coding)"""},
    {
        "role": "user",
        "content": "I'm overwhelmed. I have 5 core subjects, a 3-day Web Dev workshop, and placement drives starting next week. How do I manage this?"
    },
]

chat_response.choices[0].message.content
