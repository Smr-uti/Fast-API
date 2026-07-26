app = FastAPI()

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello Worl"}