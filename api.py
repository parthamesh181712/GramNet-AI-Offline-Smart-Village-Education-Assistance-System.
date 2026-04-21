from fastapi import FastAPI
from core.tutor import tutor_response
from core.retriever import retrieve
# import your index loader if you have one

app = FastAPI()

# ⚠️ Load your FAISS index + chunks here
# Example (modify according to your code):
from core.search_engine import load_index
index, chunks = load_index()

@app.get("/")
def home():
    return {"status": "AI Tutor Running"}

@app.post("/ask")
def ask(q: str):
    answer = tutor_response(q, chunks, index)
    return {"answer": answer}