import streamlit as st
import ollama
import time

# Page config
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS (Heavy UI)
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.chat-container {
    max-width: 900px;
    margin: auto;
}
.user-msg {
    background-color: #1f6feb;
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
    color: white;
    text-align: right;
}
.bot-msg {
    background-color: #2d333b;
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
    color: white;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    model = st.selectbox("Select Model", ["llama3.2", "llama3.2:1b"])
    temperature = st.slider("Creativity", 0.0, 1.0, 0.7)
    st.markdown("---")
    st.info("Local LLM powered by Ollama")

# Title
st.title("💬 AI Chatbot")
st.caption("Powered by Llama 3.2 (Local)")

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user instantly
    st.markdown(f'<div class="user-msg">{user_input}</div>', unsafe_allow_html=True)

    # Get response (streaming)
    response = ollama.chat(
        model=model,
        messages=st.session_state.messages,
        stream=True
    )

    bot_reply = ""
    placeholder = st.empty()

    for chunk in response:
        content = chunk["message"]["content"]
        bot_reply += content
        placeholder.markdown(f'<div class="bot-msg">{bot_reply}▌</div>', unsafe_allow_html=True)

    placeholder.markdown(f'<div class="bot-msg">{bot_reply}</div>', unsafe_allow_html=True)

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
