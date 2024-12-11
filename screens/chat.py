import streamlit as st
from time import sleep
import random
from utils.aux_functions import load_image, load_css
from api import api_openai

def chat_screen():
    load_css('style.css')
    image = load_image('logo 2.png')
    st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{image}" width="150">
    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Ruleta del amigo invisible</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat container styling
    st.markdown("""
        <style>
        .chat-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 10px;
        }
        .user-message {
            background-color: #d42426;
            color: #ffffff;
            padding: 12px 18px;
            border-radius: 15px 15px 0 15px;
            margin: 8px 0;
            max-width: 70%;
            margin-left: auto;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }
        .bot-message {
            background-color: #2d5a27;
            color: #ffffff;
            padding: 12px 18px;
            border-radius: 15px 15px 15px 0;
            margin: 8px 0;
            max-width: 70%;
            border: 1px solid #467f3f;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }
        .typing-indicator {
            color: #1b371a;
            padding: 10px;
            font-style: italic;
        }
        .stTextInput {
            position: fixed;
            bottom: 20px;
            width: 100%;
            max-width: 800px;
            background-color: #ffffff;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    # Display chat header
    st.markdown("<h2 style='text-align: center; color: #ffb703;'>Chat with AI</h2>", unsafe_allow_html=True)

    # Display chat messages
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"<div class='user-message'>{message['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='bot-message'>{message['content']}</div>", unsafe_allow_html=True)

    # Input area
    with st.container():
        def process_input():
            if st.session_state.user_input and st.session_state.user_input.strip():
                # Add user message
                user_message = st.session_state.user_input
                st.session_state.messages.append({"role": "user", "content": user_message})
                
                # Show typing indicator
                with chat_container:
                    typing_placeholder = st.empty()
                    typing_placeholder.markdown("<div class='typing-indicator'>AI is typing...</div>", unsafe_allow_html=True)
                    
                # Simulate AI processing
                sleep(random.uniform(0.5, 1.5))
                
                # Add AI response
                # ai_response = f"This is a simulated response to: {user_message}"
                response = api_openai(user_message)
                st.session_state.messages.append({"role": "assistant", "content": response})
                
                # Clear typing indicator and input
                typing_placeholder.empty()
                st.session_state.user_input = ""

        st.text_input("Message", key="user_input", on_change=process_input)
