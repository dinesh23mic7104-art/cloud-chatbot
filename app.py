from fastapi import FastAPI, Request
from pydantic import BaseModel
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Msg(BaseModel):
    message: str
    session_id: str = "default"

@app.post("/chat")
async def chat(msg: Msg):
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content": msg.message}],
        max_tokens=300
    )
    text = resp["choices"][0]["message"]["content"].strip()
    return {"reply": text}
