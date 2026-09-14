🤖 AI Chatbot (Local LLM using Ollama + Streamlit)

A modern AI chatbot application built using Streamlit and Ollama (LLaMA 3.2) that runs completely locally without any API cost. It provides a clean ChatGPT-like UI with streaming responses and conversation memory.

**✨ Features**
💬 ChatGPT-like conversational UI
🧠 Memory-based multi-turn conversation
⚡ Streaming responses (real-time typing effect)
🎛️ Model selection (llama3.2 / llama3.2:1b)
🎚️ Temperature control (creativity adjustment)
🖥️ Beautiful custom UI with dark theme
🔒 Fully local (no OpenAI API required)

**🛠️ Tech Stack**
1. Python 🐍
2. Streamlit 🎨
3. Ollama 🧠
4. LLaMA 3.2 (Local LLM)


**📸 UI Preview**


<img width="1920" height="1020" alt="chat_bot_application_UI" src="https://github.com/user-attachments/assets/a0938cc7-1135-4077-8a05-76b39a0c9613" />



**💡 How It Works**
1. User types a message in chat UI
2. Message is stored in session memory
3. Entire conversation history is sent to LLaMA via Ollama
4. Model generates streaming response
5. Response is displayed in real-time chat format
