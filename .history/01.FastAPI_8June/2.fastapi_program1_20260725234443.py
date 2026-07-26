app = FastAPI()

@app.get("/greeting")
def greeting():
    retu