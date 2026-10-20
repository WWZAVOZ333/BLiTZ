from fastapi import FastAPI
from app.api import books, categories
from app.db.db import init_engine

app = FastAPI(title="Book Store API")

@app.on_event("startup")
def on_startup():
    # Создаем таблицы при старте (если их нет)
    init_engine()

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok"}

app.include_router(categories.router)
app.include_router(books.router)