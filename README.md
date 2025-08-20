## 📌 Overview
This project is a hands-on exploration of Ollama — a tool for running large language models locally. It demonstrates how to set up custom models, process text, and integrate them with Python for building practical AI-powered applications.

## 📌 Repo Includes
-Working with Modelfiles to create and customize Ollama models
-Streaming responses from models using Python requests
-Experimenting with PDF ingestion and retrieval-augmented generation (RAG)
-A simple portfolio-style frontend (HTML/CSS/JS) that can be extended to interact with models

## 🚀 Features
**Work with Ollama models:** creating and managing custom model builds

**Use Python with APIs:** sending prompts, handling streaming responses, parsing JSON

**Document loading and RAG basics:** extracting text from PDFs, preparing embeddings for search

**Frontend development:** HTML + CSS responsive design

## 🛠️ Technologies Used
**Python**\n
**Ollama**(LLMs Manager)
**LangChain**
**Git/GitHub**

## 🧪 Running the Project Locally
**Install Ollama on your system**
1. **Clone the repository:**
```bash
git clone https://github.com/cyrusgarg/Ollama-Project.git
cd Ollama-Project
```
2. **Set Up Virtual Environment:**

```bash
python3 -m venv env
source env/bin/activate
```
3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```
4. **Start Ollama Locally**

```bash
ollama run llama3.2
```
5. **Run the Python file:**

```bash
python pdf-rag-streamlit.py
```

