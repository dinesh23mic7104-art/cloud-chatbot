from fastapi import FastAPI
from pydantic import BaseModel
import os
import openai

# Optional: Set OpenAI key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: Message):
    # Simple response (you can replace with OpenAI call if you want)
    if not openai.api_key:
        return {"reply": f"You said: {msg.message}"}

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": msg.message}],
            max_tokens=100
        )
        return {"reply": response.choices[0].message.content.strip()}
    except Exception as e:
        return {"reply": f"(Error: {e})"}
