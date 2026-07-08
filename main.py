from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

import streamlit as st
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

st.header("College Research Assistant")
parser = StrOutputParser()
college_name = st.selectbox("Select a college", [
    "Harvard University",
    "Stanford University",
    "Massachusetts Institute of Technology",
    "University of California, Berkeley",
    "University of Oxford"
])

lines = st.selectbox("How many lines?", [1,2,3,4,5,6,7,8,9,10])

user_input = st.text_input("Enter your question:")

if st.button("Submit") and user_input:
    model = ChatAnthropic(model="claude-haiku-4-5")


    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a helpful research assistant for college students. Answer politely."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "About {college}: {question}. Give {lines} lines answer.")
    ])

    chain = prompt | model | StrOutputParser()
    history = [
        HumanMessage(content="Hello, I need help with colleges."),
        AIMessage(content="Sure! Which college are you interested in?")
    ]

    response = chain.invoke({"college": college_name, "question": user_input, "lines": lines, "history": history})
    result = parser.invoke(response)

    st.write(result)
