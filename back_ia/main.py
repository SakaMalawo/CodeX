from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot.haybot import ask_haybot
import os
import fitz  # PyMuPDF, pour lire les PDF

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5178"],
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

# Nouvelle route pour upload et analyse de document
@app.post("/api/upload")
async def upload_and_analyze(file: UploadFile = File(...)):
    # Pour les fichiers texte
    if file.content_type == "text/plain":
        content = (await file.read()).decode("utf-8")
    # Pour les PDF (nécessite PyPDF2)
    elif file.content_type == "application/pdf":
        import io
        pdf_bytes = await file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        content = ""
        for page in doc:
            content += page.get_text()
    else:
        return {"error": "Format non supporté"}

    # Appel à l'IA pour évaluer le contenu
    evaluation = ask_haybot(f"Analyse ce document:\n{content[:2000]}")  # Limite à 2000 caractères pour éviter les débordements
    return {"evaluation": evaluation}

#uvicorn main:app --reload