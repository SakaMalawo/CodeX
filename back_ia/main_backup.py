from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot.haybot import ask_haybot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(msg: Message):
    reply = ask_haybot(msg.message)
    return {"reply": reply}

#rehefa hi-lancer an'ilay back: uvicorn main:app --reload