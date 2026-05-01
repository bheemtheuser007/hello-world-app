from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import httpx
import os

app = FastAPI()

GATEWAY_URL = os.getenv("GATEWAY_URL", "http://gateway:8080")

@app.get("/", response_class=HTMLResponse)
async def index():
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{GATEWAY_URL}/aggregate", timeout=3.0)
            data = r.json()
    except Exception as e:
        data = {"error": str(e)}

    return f"""<!DOCTYPE html>
<html>
<head>
  <title>Hello World App</title>
  <style>
    body {{ font-family: monospace; background: #0d1117; color: #c9d1d9; padding: 40px; }}
    h1   {{ color: #58a6ff; }}
    pre  {{ background: #161b22; padding: 20px; border-radius: 8px; border: 1px solid #30363d; }}
    .ok  {{ color: #3fb950; }}
  </style>
</head>
<body>
  <h1>🐍 Hello World – Python Microservices Trigger </h1>
  <p class="ok">✔ Frontend is running</p>
  <h3>Response from Gateway → Backend:</h3>
  <pre>{data}</pre>
</body>
</html>"""

@app.get("/health")
def health():
    return {"status": "ok"}