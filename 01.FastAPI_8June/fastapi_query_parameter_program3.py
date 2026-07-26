from fastapi import FastAPI, Path, HTTPException
import json

app = FastAPI()

def load_data():
    with open("patients.json","r") as f:
        data=json.load(f)
        return data

@app.get("/view")
def view():
    data=load_data()
    return data

@app.get("/patient/{patient_id}")
def patient(patient_id=Path(...,description="ID of patient",example="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    # return {"message": "patient not found"}
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/view/{patient_id}")
def patient_view(patient_id=Path(...,description="ID of patient",example="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    # return {"message": "patient not found"}
    raise HTTPException(status_code=404, detail="Patient not found")