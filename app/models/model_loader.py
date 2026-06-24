import joblib
from app.core.config import MODEL_PATH, PIPELINE_PATH

model = None
pipeline = None

def load_model():
    global model, pipeline
    if model is None:
        model = joblib.load(MODEL_PATH)
        pipeline = joblib.load(PIPELINE_PATH)
    return model, pipeline