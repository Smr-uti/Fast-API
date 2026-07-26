from fastaapp = FastAPI()

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello World"}