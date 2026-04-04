from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data

@app.get('/')
def hello():
    return {'message': 'Hello'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(
    patient_id: str = Path(..., description='patient ID required', example='P001')
):
    data = load_data()

    patient = data.get(patient_id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient

@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description='sort basis on height, weight or bmi'),
    order: str = Query('asc', description='sort based on asc or desc')
):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field select from {valid_fields}"
        )

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400,
            detail="Invalid field select between asc and desc"
        )

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data