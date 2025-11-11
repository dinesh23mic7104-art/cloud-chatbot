from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Chatbot backend is running successfully 🚀"}

@app.post("/chat")
def chat(msg: Message):
    return {"reply": f"You said: {msg.message}"}
