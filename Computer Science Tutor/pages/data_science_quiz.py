import streamlit as st
import openai
from openai import OpenAI

client = OpenAI(api_key="nuykllll")

def generate_ds_questions(difficulty):
    completion = client.chat.completions.create(
      model="gpt-5-nano",
      messages=[
      {"role": "system", "content": "You are a Computer Science tutor. Create exactly 5 Data Science questions (a mix of multiple choice and fill in the blanks) based on the specified difficulty level. Format them clearly as a numbered list. Provide only the questions and any multiple choice options if applicable, do not provide the answers."},
      {"role": "user", "content": f"Create 5 {difficulty} Data Science questions."}
      ]
    )
    return completion.choices[0].message.content.strip()

def check_ds_answers(questions, user_answers):
    completion = client.chat.completions.create(
      model="gpt-5-nano",
      messages=[
      {"role": "system", "content": "You are a Computer Science tutor. You will be given 5 Data Science questions and a set of answers provided by the user. Evaluate each one, state if it's correct or wrong along with the actual correct answer, and provide a brief helpful explanation."},
      {"role": "user", "content": f"Questions:\n{questions}\n\nUser Answers:\n{user_answers}\n\nEvaluate the correctness and provide feedback for each question:"}
      ]
    )
    return completion.choices[0].message.content.strip()

def app():
    st.header('Data Science Quiz')
    st.write('Test your Data Science knowledge! Generate 5 questions (MCQ or Fill-in-the-blank) and submit your answers.')

    difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

    if 'ds_questions' not in st.session_state:
        st.session_state.ds_questions = None
    if 'ds_user_response' not in st.session_state:
        st.session_state.ds_user_response = ''

    if st.button('Generate Quiz'):
        with st.spinner("Generating 5 questions..."):
            st.session_state.ds_questions = generate_ds_questions(difficulty)
    
    if st.session_state.ds_questions:
        st.subheader('Quiz Questions:')
        st.write(st.session_state.ds_questions)

        user_response = st.text_area('Write your answers here (e.g., as a numbered list):', key="ds_response", height=150)

        if st.button('Submit Answers'):
            if user_response:
                st.session_state.ds_user_response = user_response
                with st.spinner("Evaluating your answers..."):
                    feedback = check_ds_answers(st.session_state.ds_questions, user_response)
                st.subheader('Feedback:')
                st.write(feedback)
            else:
                st.error("Please enter your answers before submitting.")
