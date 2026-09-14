A simple and powerful AI-powered PDF summarizer built using Streamlit, PyMuPDF, and Ollama (LLaMA 3.2).
It extracts text from uploaded PDFs and generates intelligent summaries using a fully local LLM, with no API costs.

**✨ Features**
📤 Upload PDF file via UI
📄 Extract text from PDF using PyMuPDF
🧠 AI-powered summarization using LLaMA (Ollama)
⚡ Fast local inference (no internet/API required)
🎨 Clean and modern Streamlit UI
📄 Expandable raw PDF text viewer
🔒 Fully offline and privacy-friendly


**🛠️ Tech Stack**
1. Python 🐍
2. Streamlit 🎨
3. PyMuPDF (fitz) 📄
4. Ollama 🧠


**LLaMA 3.2 (Local LLM)**
🚀 Installation
1. Install Ollama

**Download Ollama:**
👉 https://ollama.com

**Run model:**
ollama run llama3.2


**2. Clone Repository**
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

**3. Install Dependencies**
pip install streamlit pymupdf ollama

**4. Run Application**
streamlit run app.py

**🧠 How It Works**
1. User uploads a PDF file
2. PyMuPDF extracts text from all pages
3. Entire text is sent to LLaMA via Ollama
4. Model generates a structured summary
5. Summary is displayed in a clean UI

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/18a9372b-929f-4a0f-86b2-dbf70c2cca45" />


**⚙️ UI Components**
1. 📌 Title + Branding
2. 📤 File uploader
3. 🧠 AI processing spinner
4. 📝 Summary output box
5. 📄 Expandable raw text viewer
