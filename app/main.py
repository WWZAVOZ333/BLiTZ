from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import books, categories
from app.db.db import init_engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Действия при запуске (создаем таблицы, если их нет)
    init_engine()
    yield
    # Действия при выключении (если нужны)

app = FastAPI(title="Book Store API", lifespan=lifespan)

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok"}

app.include_router(categories.router)
app.include_router(books.router)