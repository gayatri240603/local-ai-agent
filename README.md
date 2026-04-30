# Local AI Agent (RAG with Ollama)

This is a local AI project built using:
- Ollama (TinyLlama)
- LangChain
- ChromaDB

## Features
- Retrieval-Augmented Generation (RAG)
- Works fully offline
- Uses restaurant review dataset

## Limitations
- Uses lightweight model (TinyLlama) due to low RAM
- May produce incorrect answers in some cases

## How to Run

```bash
pip install -r requirements.txt
python main.py
Future Improvements
Better model (Llama3 / Mistral)
Improved retrieval filtering
Web search integration