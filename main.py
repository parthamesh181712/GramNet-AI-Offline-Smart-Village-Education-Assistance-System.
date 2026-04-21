from fastapi import FastAPI
from pydantic import BaseModel
from core.tutor import tutor_response

app = FastAPI(title="AI Tutor Backend")

class Query(BaseModel):
    text: str

@app.post("/predict")
def predict(data: Query):
    response = tutor_response(data.text)
    return response

@app.get("/")
def home():
    return {"status": "AI Tutor Backend Running 🚀"}
