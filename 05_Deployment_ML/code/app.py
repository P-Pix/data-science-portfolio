from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("../models/credit_card_default_model.pkl")

class InputData(BaseModel):
    LIMIT_BAL: int
    SEX: int
    EDUCATION: int
    MARRIAGE: int
    AGE: int
    PAY_0: int
    PAY_2: int
    PAY_3: int
    PAY_4: int
    PAY_5: int
    PAY_6: int
    BILL_AMT1: int
    BILL_AMT2: int
    BILL_AMT3: int
    BILL_AMT4: int
    BILL_AMT5: int
    BILL_AMT6: int
    PAY_AMT1: int
    PAY_AMT2: int
    PAY_AMT3: int
    PAY_AMT4: int
    PAY_AMT5: int
    PAY_AMT6: int
    default_payment_next_month: int

@app.post("/predict")
def predict(data: InputData):
    X = np.array([[data.LIMIT_BAL, data.SEX, data.EDUCATION, data.MARRIAGE, data.AGE, data.PAY_0, data.PAY_2, data.PAY_3, data.PAY_4, data.PAY_5, data.PAY_6, data.BILL_AMT1, data.BILL_AMT2, data.BILL_AMT3, data.BILL_AMT4, data.BILL_AMT5, data.BILL_AMT6, data.PAY_AMT1, data.PAY_AMT2, data.PAY_AMT3, data.PAY_AMT4, data.PAY_AMT5, data.PAY_AMT6]])
    y_pred = model.predict(X)
    return {"prediction": int(y_pred[0])}
