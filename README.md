# 🩺 ReportIQ AI (Medical Report Analysis Platform)

AI-powered platform to analyze medical reports and provide intelligent health insights.

---

## Features | Tech Stack | Installation | Project Structure | Contributing | Author

## Usage Demo

---

## 🌟 Features

### AI-based Architecture
- Analysis Agent: AI-powered medical report analysis with contextual understanding and built-in medical knowledge.
- Chat Agent: RAG-powered follow-up Q&A using FAISS vector search and HuggingFace embeddings.
- Multi-model inference using Groq with automatic fallback (Primary → Secondary → Tertiary → Backup).
- Chat Sessions: Create multiple report analysis sessions with report history stored securely in Supabase.
- Report Sources: Upload your own medical PDF or use the built-in sample report for testing.
- PDF Processing: Supports PDF uploads up to 20MB with automatic validation and text extraction.
- Daily Analysis Limit: Configurable daily report analysis limit with sidebar usage tracking.
- Secure Authentication: User login, signup, session management, and authentication powered by Supabase.
- Session History: Access, switch, or delete previous analysis sessions with persistent chat history.
- Modern Interface: Responsive Streamlit application with clean dashboard and interactive user experience.

---

## 🛠️ Tech Stack

### Frontend
- Streamlit (1.42+)

### AI / LLM
- Groq API
- Model Manager with Multi-model Fallback

**Primary**
- meta-llama/llama-4-maverick-17b-128e-instruct

**Secondary**
- llama-3.3-70b-versatile

**Tertiary**
- llama-3.1-8b-instant

**Fallback**
- llama3-70b-8192

### AI Chat
- LangChain
- HuggingFace Embeddings (all-MiniLM-L6-v2)
- FAISS Vector Store
- Retrieval-Augmented Generation (RAG)

### Database
- Supabase (PostgreSQL)

Tables:
- users
- chat_sessions
- chat_messages

### Authentication
- Supabase Auth

### PDF Processing
- PDFPlumber
- filetype

### Libraries
- LangChain
- LangChain Community
- LangChain HuggingFace
- LangChain Text Splitters
- sentence-transformers
- FAISS (CPU)
