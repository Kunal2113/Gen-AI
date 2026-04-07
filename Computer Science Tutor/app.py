import streamlit as st
from pages import home, sql_translation, data_science_quiz, image_comprehension

PAGES = {
    "Home": home,
    "SQL Translation": sql_translation,
    "Data Science Quiz": data_science_quiz,
    "AI & ML Image Speech Comprehension": image_comprehension
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
