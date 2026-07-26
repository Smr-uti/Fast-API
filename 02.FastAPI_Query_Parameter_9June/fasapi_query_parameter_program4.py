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

@app.get("/sort")
def sort_patient(sort_by:str,
                 order:str):
    valid_fields=["height","weight","bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid field selection, please select from height,weight,bmi")

    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400, detail="Invalid order selection, please select between asc and desc")

    data = load_data()
    sort_order=True if order=="desc" else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by), reverse=sort_order)
    return sorted_data
