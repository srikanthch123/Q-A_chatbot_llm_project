
import streamlit as st

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title='Conversational Q&A Chatbot')


st.header("Hey, Let's Chat")

chat = ChatOpenAI(temperature=0.5)

if 'key' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content='You are a comedian AI assistant')
    ]


def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content


input_text = st.text_input("Input ", key='input')

response = get_chatmodel_response(input_text)


submit_button = st.button('Ask the question')


if submit_button:
    st.subheader("The Response is")
    st.write(response)
