import streamlit as st
import openai
from openai import OpenAI

client = OpenAI(api_key="tyyyyy4e5rthjus")

def generate_sql_problem():
    completion = client.chat.completions.create(
      model="gpt-5-nano",
      messages=[
      {"role": "system", "content": "You are a Computer Science tutor. Generate a short, realistic SQL problem. Provide a simple table schema, and an English question asking to write a query for that schema."},
      {"role": "user", "content": "Please generate a SQL practice problem."}
      ]
    )
    return completion.choices[0].message.content.strip()

def check_sql_answer(problem, user_sql):
    completion = client.chat.completions.create(
      model="gpt-5-nano",
      messages=[
      {"role": "system", "content": "You are a Computer Science tutor evaluating a student's SQL query. Given the problem and the user's SQL, evaluate the correctness, point out any syntax or logical errors, and provide supportive feedback."},
      {"role": "user", "content": f"Problem:\n{problem}\n\nUser's SQL:\n{user_sql}\n\nEvaluate the correctness of the SQL and provide feedback."}
      ]
    )
    return completion.choices[0].message.content.strip()

def app():
    st.header('SQL Translation Practice')
    st.write('Test your database skills. Read the problem below and write the corresponding SQL query.')

    if 'sql_problem' not in st.session_state:
        st.session_state.sql_problem = None
    if 'user_sql_input' not in st.session_state:
        st.session_state.user_sql_input = ''

    if st.button('Generate New Problem'):
        with st.spinner("Generating problem..."):
            st.session_state.sql_problem = generate_sql_problem()
            st.session_state.user_sql_input = ''
    
    if st.session_state.sql_problem:
        st.subheader('SQL Problem:')
        st.write(st.session_state.sql_problem)

        user_sql = st.text_area('Your SQL Query:', key="sql_input", height=150)

        if st.button('Submit SQL for Feedback'):
            if user_sql:
                st.session_state.user_sql_input = user_sql
                with st.spinner("Evaluating your query..."):
                    feedback = check_sql_answer(st.session_state.sql_problem, user_sql)
                st.subheader('AI Feedback:')
                st.write(feedback)
            else:
                st.error("Please enter a SQL query before checking.")
