from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message" : "Hello World!"}

@app.get("/about")
def about():
    return {"new_message": "This is out first FastAPI program!"}


