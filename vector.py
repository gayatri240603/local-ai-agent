from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# ---- File path ----
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "realistic_restaurant_reviews.csv")

# ---- Load CSV ----
df = pd.read_csv(file_path)

# ---- Embedding model ----
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# ---- Vector DB location ----
db_location = os.path.join(base_dir, "chroma_langchain_db")

# ---- Prepare documents ----
documents = []
ids = []

for i, row in df.iterrows():
    document = Document(
        page_content=str(row["Title"]) + " " + str(row["Review"]),
        metadata={
            "rating": row["Rating"],
            "date": row["Date"]
        }
    )
    documents.append(document)
    ids.append(str(i))

print("Adding documents:", len(documents))

# ---- Create vector store ----
vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

# ---- Add documents ----
vector_store.add_documents(documents=documents, ids=ids)

print("✅ Vector DB ready!")