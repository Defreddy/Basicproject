from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

@app.get("/product")
async def root():
    return {"message": "This is a product"}

@app.get("/cve")
async def root():
    return {"message": "This is a cve"}

#@app.post("/cve")
#async def root():
#    return {"message": "Hello World"}

