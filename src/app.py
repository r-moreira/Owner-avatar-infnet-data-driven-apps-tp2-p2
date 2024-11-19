from fastapi import FastAPI
import os
from dotenv import load_dotenv
from .routers.chat_route import router as chat_router

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

print(f"Loading .env from: {env_path}")

load_dotenv(env_path)

app = FastAPI()

app.include_router(chat_router, prefix="/chat")

@app.get("/")
def hello_message():
    return {"Hello": "FastAPI"}