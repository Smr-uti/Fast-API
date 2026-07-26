from fastapi import FastAapp = FastAPI()

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello World"}