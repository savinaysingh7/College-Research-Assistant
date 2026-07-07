from dotenv import load_dotenv

# Load .env from same folder as this script
load_dotenv()

from langchain_anthropic import ChatAnthropic

import streamlit as st

st.header("College Research Assistant")
user_input = st.text_input("Enter the prompt: ")
if st.button("Submit"):
    model = ChatAnthropic(
        model="claude-haiku-4-5"
    )

    results = model.invoke(user_input)
    st.write(results.content)
