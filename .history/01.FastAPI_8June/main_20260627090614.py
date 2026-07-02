from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello world"}

@app.get("/about")
def about():
    return {"new_messgae":"this is our first fastapi program"}







# www.website_name/trains