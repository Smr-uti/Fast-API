app = 

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello World"}