from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

import streamlit as st
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

st.header("College Research Assistant")
parser = StrOutputParser()
college_name = st.selectbox("Select a college", [
    "Harvard University",
    "Stanford University",
    "Massachusetts Institute of Technology",
    "University of California, Berkeley",
    "University of Oxford"
])

user_input = st.text_input("Enter your question:")

if st.button("Submit") and user_input:
    model = ChatAnthropic(model="claude-haiku-4-5")

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful research assistant for college students. Answer politely."),
        ("human", "About {college}: {question}")
    ])

    chain = prompt | model | StrOutputParser()
    response = chain.invoke({"college": college_name, "question": user_input})
    result = parser.invoke(response)

    st.write(result)
