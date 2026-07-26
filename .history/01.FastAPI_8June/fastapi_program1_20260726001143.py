from fastapi import FastAPI

app = FastAPI()

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello World"}

@app.get("/about_us")
def about_us()
    return {""}