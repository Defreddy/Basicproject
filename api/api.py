from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

