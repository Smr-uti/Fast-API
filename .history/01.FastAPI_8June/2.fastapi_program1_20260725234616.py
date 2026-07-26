app = FastAP

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello World"}