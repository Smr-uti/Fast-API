from fastapi import FastAPIapp = FastAPI()

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello World"}