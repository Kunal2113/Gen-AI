pip install openAI

import openai

openai.api_key = "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"

import openai

conversation_length = 0
max_conversations = 10
message_history = [
    {"role": "system", "content": '''You are a Travel Itinerary Planner.
    You MUST NOT provide a final itinerary until you have these 4 details:
    1. Destination, 2. Budget, 3. No. of People, 4. Travel Dates.
    If details are missing, your response must ONLY be a polite request for the missing items.
    Once all 4 are provided, generate a detailed day-wise itinerary.
    If a user asks a Mathematical question or any arithmetic or any general science related question just say  "I am not able to answer that ".'''},
    {"role": "user", "name": "example_user", "content": "I want to go to Paris!"},
    {"role": "assistant", "name": "example_assistant", "content": "Paris sounds lovely! To help me plan the perfect trip, could you please tell me your budget (Economy, Mid-range, or Luxury), how many people are traveling, and your intended travel dates?"},
    {"role": "user", "name": "example_user", "content": "It's for 2 people, luxury budget, in June."},
    {"role": "assistant", "name": "example_assistant", "content": "Perfect! I have all the details. Here is your luxury 7-day itinerary for Paris..."},
    {"role": "user", "content": "I need help planning a trip."}
]

while conversation_length < max_conversations:

    chat_completion = openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=message_history
    )

    chat_response = chat_completion.choices[0].message.content

    print("\nTravel Agent:")
    print(chat_response)
    print("\n")

    message_history.append({"role": "assistant", "content": chat_response})


    conversation_length += 1
    if conversation_length >= max_conversations:
        print("End of planning session. Safe travels!")
        break


    user_input = input("You: ")

    if "exit" in user_input.lower():
        print("Travel Agent: Goodbye! Happy exploring.")
        break


    message_history.append({"role": "user", "content": user_input})

chat_response.choices[0].message.content
