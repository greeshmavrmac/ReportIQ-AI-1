# 🩺 ReportIQ AI

### AI-Powered Medical Report Analysis & Intelligent Health Insights Platform

ReportIQ AI is an intelligent healthcare application that analyzes medical reports using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG). It helps users understand complex laboratory reports, identifies abnormal findings, provides personalized health insights, and answers follow-up questions through an interactive AI assistant.

---

## 🚀 Key Features

### 📄 AI Medical Report Analysis
- Upload PDF medical reports for instant AI analysis
- Detect abnormal laboratory values automatically
- Generate easy-to-understand health summaries
- Explain medical terminology in simple language

### 🤖 Intelligent AI Assistant
- Interactive chatbot for report-related questions
- Context-aware conversations using Retrieval-Augmented Generation (RAG)
- Personalized responses based on uploaded reports
- Multi-turn conversation support

### 📊 Smart Health Insights
- Highlight abnormal biomarkers
- Explain possible health conditions
- Lifestyle and wellness recommendations
- Follow-up monitoring suggestions

### 💾 Session Management
- Secure user authentication
- Multiple report analysis sessions
- Chat history persistence
- Session recovery after login

### 📁 Medical Report Processing
- PDF upload support
- Automatic text extraction
- File validation
- Medical content verification

### 🔒 Security
- Secure Supabase Authentication
- Protected user sessions
- Encrypted API communication
- Secure cloud database

---

# 🛠 Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## AI & Machine Learning
- Groq API
- Llama Models
- LangChain
- HuggingFace Embeddings
- FAISS Vector Database
- Retrieval-Augmented Generation (RAG)

## Database
- Supabase PostgreSQL

## Authentication
- Supabase Auth

## PDF Processing
- PDFPlumber
- FileType

---

# ⚡ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/ReportIQ-AI.git

cd ReportIQ-AI
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment

Create

```
.streamlit/secrets.toml
```

```toml
SUPABASE_URL="YOUR_SUPABASE_URL"
SUPABASE_KEY="YOUR_SUPABASE_KEY"
GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

## Setup Database

Run the SQL script located in

```
public/db/script.sql
```

inside your Supabase SQL Editor.

## Start Application

```bash
streamlit run src/main.py
```

---

# 📂 Project Structure

```
ReportIQ-AI
│
├── src
│   ├── auth
│   ├── agents
│   ├── components
│   ├── services
│   ├── config
│   ├── utils
│   └── main.py
│
├── public
│   └── db
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 💡 Workflow

1. Login or Register
2. Create a New Analysis Session
3. Upload a Medical Report
4. AI Analyzes the Report
5. Receive Personalized Health Insights
6. Ask Follow-up Questions
7. Save Session History

---

# 🎯 Future Enhancements

- Multi-language Support
- OCR for Scanned Reports
- Doctor Recommendation System
- Medical Trend Visualization
- Health Risk Prediction
- Mobile Application
- Voice Assistant

---

# 👩‍💻 Developer

**Veeramachineni Greeshma**

B.Tech Data Science Student

---

# 📜 License

This project is released under the MIT License.

---

## ⭐ If you found this project useful, consider giving it a star!

