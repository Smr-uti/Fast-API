from fastapi import Fastapp = FastAPI()

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello World"}