from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patients.json","r") as f:
        data=json.load(f)
        return data

@app.get("/greeting")
def greeting():
    return {"greeting": "Hello World"}

@app.get("/about_us")
def about_us():
    return {"about_us": "we are learning FastAPI"}

@app.get("/view")
def view():
    data=load_data()
    return data

