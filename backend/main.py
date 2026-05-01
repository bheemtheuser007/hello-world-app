from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from the Backend!", "service": "backend"}

@app.get("/health")
def health():
    return {"status": "ok"}