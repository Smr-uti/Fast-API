from fastapi import Faapp = FastAPI()

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello World"}