from fastapi impapp = FastAPI()

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello World"}