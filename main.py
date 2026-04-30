from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma
import os

# ---- Load vector DB ----
base_dir = os.path.dirname(os.path.abspath(__file__))
db_location = os.path.join(base_dir, "chroma_langchain_db")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)
print("DB count:", vector_store._collection.count())

retriever = vector_store.as_retriever(search_kwargs={"k": 8})

# ---- LLM ----
llm = OllamaLLM(model="tinyllama")

# ---- Chat loop ----
while True:
    query = input("\nAsk something (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    # Retrieve relevant docs
    enhanced_query = """
    vegan pizza vegan cheese dairy-free vegetarian plant-based cashew cheese no-cheese option vegan review
    """
    docs = vector_store.similarity_search(enhanced_query, k=5)
    print("Docs count:", len(docs))
    print("\n📄 Sources used:")
    for doc in docs:
        print("-", doc.page_content[:100])

    context = "\n\n".join([
        f"{doc.metadata.get('rating', '')}⭐: {doc.page_content}"
        for doc in docs
    ])

    prompt = f"""
You are a strict restaurant review analyst.

Rules:
- Use ONLY the given context
- Do NOT add any new information
- If something is not mentioned, say "Not mentioned"
- Do NOT assume or generalize

Give output in this format:

Overall Sentiment: (positive / negative / mixed)

Key Points:
- point 1
- point 2

Final Conclusion:
- short summary based ONLY on context

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    print("\n🤖 Answer:\n", response)    