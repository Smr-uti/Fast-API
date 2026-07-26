app = FastAPI()

@app.get("/greeting")
def greeting():
    return {"gree"}