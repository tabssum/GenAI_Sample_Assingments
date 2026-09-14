🤖 AI Chatbot (Local LLM using Ollama + Streamlit)

A modern AI chatbot application built using Streamlit and Ollama (LLaMA 3.2) that runs completely offline on your local machine. It provides a ChatGPT-like experience with streaming responses, session memory, and a clean interactive UI.

✨ Features
💬 ChatGPT-style conversational UI
🧠 Multi-turn conversation memory (session-based)
⚡ Real-time streaming responses
🎛️ Model selection (llama3.2 / llama3.2:1b)
🎚️ Adjustable creativity (temperature control)
🎨 Custom dark-themed UI
🔒 Fully local (no API keys required)


🛠️ Tech Stack
1. Python 🐍
2. Streamlit 🎨
3. Ollama 🧠
4. LLaMA 3.2 (Local LLM)

📸 UI Preview
see chat_bot_application_UI.png


🚀 Installation
1. Install Ollama

Download and install Ollama:
👉 https://ollama.com

Pull the model:

ollama run llama3.2

2. Clone Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
3. Install Dependencies
pip install streamlit ollama
4. Run Application
streamlit run app.py

🧠 How It Works
1. User enters a message in the chat box
2. Message is stored in session memory (st.session_state)
3. Full conversation history is sent to LLaMA via Ollama
4. Model generates a streaming response token-by-token
5. Response is displayed in real time UI
⚙️ Configuration Options

Inside the sidebar:

Model Selection
llama3.2
llama3.2:1b
Temperature Control
0.0 → More focused responses
1.0 → More creative responses


