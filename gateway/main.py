from fastapi import FastAPI
import httpx
import os

app = FastAPI()

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8080")

@app.get("/")
def hello():
    return {"message": "Hello from the Gateway!", "service": "gateway"}

@app.get("/aggregate")
async def aggregate():
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{BACKEND_URL}/", timeout=3.0)
            backend = r.json()
    except Exception as e:
        backend = {"error": str(e)}
    return {"gateway": "Hello from Gateway!", "backend": backend}

@app.get("/health")
def health():
    return {"status": "ok"}