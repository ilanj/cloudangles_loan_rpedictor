import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class RequestModel(BaseModel):
    feature1 : int
    feature2 : int
    feature3 : int
    feature4 : int
    feature5 : int
    feature6 : int
    feature7 : int
    feature8 : int
    feature9 : int
    feature10 : int
    feature11 : int
    feature12 : int
    feature13 : int
    feature14 : int
    feature15 : int
    feature16 : int
    feature17 : int
    feature18 : int
    feature19 : int
    feature20 : int
    feature21 : int
    feature22 : int
    feature23 : int
    feature24: int
    feature25: int
    feature27: int
    feature28: int
    feature29: int
    feature30: int
    feature31: int
    feature32: int
    feature33: int
    feature34: int
    feature35: int
    feature36: int
    feature37: int

model = joblib.load("rf_model.joblib.pkl")

@app.post("/predict")
async def get_fact(req: RequestModel):
    target = model.predict(req.__dict__)
    return {"prediction": target}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")