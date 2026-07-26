from fastapi import app = FastAPI()

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello World"}