pip install openAI
import openai
openai.api_key = "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"
conversation_length = 0
max_conversations = 5
message_history = [
    {"role": "system", "content": '''You are an AI tutor that assists school students with math homework problems. You never reveal the right answer to the student. You ask probing questions to identify where the student might be needing help, provide hints and guidance, and provide directional feedback to indicate if the student is moving in the right direction.'''},
    {"role": "user", "name": "example_user", "content": "Help me solve the equation 3x - 9 = 21."},
    {"role": "assistant", "name": "example_assistant", "content": "Sure! Try moving the 9 to the right hand side of the equation. What do you get?"},
    {"role": "user", "name": "example_user", "content": "3x = 12"},
    {"role": "assistant", "name": "example_assistant", "content": "'Well, there seems to be a mistake. When you move 9 to the right hand side, you need to change its sign. Can you try again?'"},
    {"role": "user", "name": "example_user", "content": "3x = 30"},
    {"role": "assistant", "name": "example_assistant", "content": "That looks good, great job! Now, try to divide both sides by 3. What do you get?"},
    {"role": "user", "name": "example_user", "content": "x = 10"},
    {"role": "user", "content": "Help me solve the equation x + 10 = 2x"}
]

while conversation_length < max_conversations:
    user_input = input()


    if "exit" in user_input.lower():
        print("AI Tutor: Exiting the program!")
        break

    message_history.append({"role": "user", "content": user_input})

    chat_response = openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages = message_history).choices[0].message.content

    print("\n", "AI Tutor:")
    print(chat_response)
    print("\n")

    message_history.append({"role": "assistant", "content": chat_response})
    conversation_length = conversation_length + 1

    chat_response.choices[0].message.content
