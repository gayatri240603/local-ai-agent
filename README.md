#  Local AI Agent (RAG with Ollama)

A lightweight **offline AI system** that answers questions using a restaurant reviews dataset. Built using **Retrieval-Augmented Generation (RAG)** with local models — no API required.

---

##  Overview

This project demonstrates how to build a **local AI assistant** that:

* Retrieves relevant data from a vector database (ChromaDB)
* Uses embeddings for semantic search
* Generates answers using a local LLM (TinyLlama via Ollama)

> Designed with **low-RAM systems in mind**.

---

##  Tech Stack

* **LLM:** TinyLlama (via Ollama)
* **Embeddings:** mxbai-embed-large
* **Vector DB:** ChromaDB
* **Framework:** LangChain
* **Language:** Python

---

##  Features

*  Fully offline (no OpenAI / paid APIs)
*  RAG pipeline (retrieval + generation)
*  Semantic search over restaurant reviews
*  Simple CLI-based chat interface
*  Optimized for low-resource environments

---

##  Project Structure

```
local-ai-agent/
│── main.py
│── realistic_restaurant_reviews.csv
│── chroma_langchain_db/   (ignored in git)
│── requirements.txt
│── README.md
```

---

##  How to Run

### 1. Clone the repo

```
git clone https://github.com/YOUR_USERNAME/local-ai-agent.git
cd local-ai-agent
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run Ollama models

Make sure Ollama is installed and running:

```
ollama run tinyllama
ollama pull mxbai-embed-large
```

### 5. Run the project

```
python main.py
```

---

##  Example Queries

* "How are the vegan options?"
* "What do people say about cheese quality?"
* "Is this restaurant good for dietary restrictions?"

---

##  Limitations

* Uses **TinyLlama (small model)** → may produce incorrect or generic answers
* Retrieval may sometimes return irrelevant documents
* No real-time data (static dataset only)
* No location-based search ("near me" not supported)

---

##  Future Improvements

*  Upgrade to larger models (Llama3 / Mistral)
*  Improve retrieval (filtering + reranking)
*  Add query understanding (intent detection)
*  Add web search integration
*  Build a UI (Streamlit)

---

##  Key Learning

This project focuses on:

* Building RAG systems under **resource constraints**
* Understanding **embedding + retrieval behavior**
* Handling **LLM limitations (hallucination, formatting issues)**

---

##  Note

This is an **experimental project** built for learning and internship preparation. The focus is on system design and debugging rather than production-level accuracy.

---



## ⭐ If you found this useful

Give it a star ⭐ on GitHub!
