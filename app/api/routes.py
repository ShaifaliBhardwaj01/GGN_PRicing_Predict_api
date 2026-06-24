from fastapi import APIRouter
from app.services.predict_service import predict
from app.services.train_service import train_model

router = APIRouter()

@router.get("/")
def home():
    return {"message": "API running"}

@router.get("/train")
def train():
    return {"status": train_model()}

@router.post("/predict")
def get_prediction(data: dict):
    return {"prediction": predict(data)}