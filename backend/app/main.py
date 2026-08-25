from fastapi import FastAPI
from sqlmodel import SQLModel

from app.database import engine
from app import models


app = FastAPI(
    title="AI-Powered RAG Knowledge Assistant",
    version="0.1.0"
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/")
def root():
    return {
        "message": "AI-Powered RAG Knowledge Assistant API"
    }