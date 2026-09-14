import streamlit as st
import pymupdf  # PyMuPDF
import ollama

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="PDF Summary AI",
    page_icon="📄",
    layout="wide"
)

# ---------------- CUSTOM UI ----------------
st.markdown("""
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #4CAF50;
    }
    .sub {
        text-align: center;
        color: gray;
        margin-bottom: 20px;
    }
    .box {
        background-color: #111827;
        padding: 20px;
        border-radius: 12px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📄 PDF Summary AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Powered by Local LLaMA (Ollama)</div>', unsafe_allow_html=True)

# ---------------- PDF EXTRACT ----------------
def extract_text(pdf_file):
    doc = pymupdf.open(stream=pdf_file.read(), filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return text


# ---------------- SUMMARIZE ----------------
def summarize_text(text):
    prompt = f"""
    You are an expert AI assistant.

    Read the following document and provide a clear, structured summary:

    {text}

    Summary:
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


# ---------------- UI ----------------
uploaded_file = st.file_uploader("📤 Upload your PDF file", type=["pdf"])

if uploaded_file:

    with st.spinner("📄 Reading PDF..."):
        text = extract_text(uploaded_file)

    if len(text.strip()) == 0:
        st.error("❌ No text found in PDF (it may be scanned image PDF)")
    else:
        st.success("✅ PDF loaded successfully!")

        st.subheader("🧠 Generating Summary...")

        with st.spinner("AI is thinking..."):
            summary = summarize_text(text)

        st.markdown("## 📝 Summary")
        st.markdown(f'<div class="box">{summary}</div>', unsafe_allow_html=True)

        # Optional raw text viewer
        with st.expander("📄 View Extracted Text"):
            st.text_area("PDF Content", text, height=300)

else:
    st.info("👆 Upload a PDF to get AI summary")