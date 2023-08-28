# 1. Create an App that shows the dashboard page in UI. You make skip the UI if you want. The  format of the page is attached 
# 2. Sample data is attached in excel. 
# 3. Create a Fast API backend and database that can use the data and provide an API output for the UI to consume in the charts.


import uvicorn
from fastapi import FastAPI, Depends
from database import SessionLocal, engine
from sqlalchemy.orm import Session

from sqlalchemy import text
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"go to ": "http://127.0.0.1:8000/docs"}

@app.get("/get_all_data")
def get_all_data(db: Session = Depends(get_db)):
    query = text("SELECT * FROM TableData;")
    result = db.execute(query)
    data = result.fetchall()
    print(data)
 # Preprocess data for serialization
    processed_data = [
        (str(item[0]), item[1], item[2], item[3], item[4], item[5], item[6])
        for item in data
    ]

    try:
        json_data = jsonable_encoder(processed_data)
        return json_data
    except ValueError as e:
        return {"error": str(e)}

@app.get("/get_new_npa_accounts")
def get_new_npa_accounts(db: Session = Depends(get_db)):
    query = text("SELECT customer_name,days_overdue,amount_outstanding FROM TableData WHERE chart_type = 'New NPA Accounts';")
    result = db.execute(query)
    data = result.fetchall()
    print(data)
 # Preprocess data for serialization
    processed_data = [
        (str(item[0]), item[1], item[2])
        for item in data
    ]

    try:
        json_data = jsonable_encoder(processed_data)
        return json_data
    except ValueError as e:
        return {"error": str(e)}

@app.get("/get_new_accounts_with_recovery")
def get_new_accounts_with_recovery(db: Session = Depends(get_db)):
    query = text("SELECT customer_name,recovery,amount_outstanding FROM TableData WHERE chart_type = 'NPA Accounts with recovery';")
    result = db.execute(query)
    data = result.fetchall()
    print(data)
 # Preprocess data for serialization
    processed_data = [
        (str(item[0]), item[1], item[2])
        for item in data
    ]

    try:
        json_data = jsonable_encoder(processed_data)
        return json_data
    except ValueError as e:
        return {"error": str(e)}
    
@app.get("/get_new_sma_accounts")
def get_new_sma_accounts(db: Session = Depends(get_db)):
    query = text("SELECT customer_name,days_overdue,amount_outstanding FROM TableData WHERE chart_type = 'New SMA Accounts';")
    result = db.execute(query)
    data = result.fetchall()
    print(data)
 # Preprocess data for serialization
    processed_data = [
        (str(item[0]), item[1], item[2])
        for item in data
    ]

    try:
        json_data = jsonable_encoder(processed_data)
        return json_data
    except ValueError as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)