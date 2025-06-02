# chat_ui.py
import os

import requests
import streamlit as st
from PIL import Image


def get_assistant_answer() -> str:
    url = os.getenv("ASSISTANT_API_URL", "http://localhost:8000/chat/")
    payload = {"conversation": st.session_state.conversation}
    response = requests.post(url, json=payload, timeout=60)
    return response.json()["assistant_response"]


@st.cache_data
def load_icon():
    file_path = "data/pokedex_icon.png"
    return Image.open(file_path)


@st.cache_data
def load_banner():
    file_path = "data/banner.png"
    return Image.open(file_path)


pokedex_icon = load_icon()
pokedex_banner = load_banner()

st.image(pokedex_banner)

if "conversation" not in st.session_state:
    st.session_state.conversation = []

for msg in st.session_state.conversation:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant", avatar=pokedex_icon):
            st.markdown(msg["content"])

prompt = st.chat_input("Ask question to the Pokédex...")

if prompt:
    st.session_state.conversation.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    response = get_assistant_answer()
    st.session_state.conversation.append(response)
    with st.chat_message("assistant", avatar=pokedex_icon):
        st.markdown(response["content"])
    # clear conversation if it exceeds 10 messages
    st.session_state.conversation = st.session_state.conversation[-10:]
