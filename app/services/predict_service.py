# import joblib
# import pandas as pd
# import os
# from config import MODEL_FILE, PIPELINE_FILE
# from train import train_model

# model = None
# pipeline = None


# def load_model():
#     global model, pipeline

#     if not os.path.exists(MODEL_FILE):
#         train_model()

#     if model is None:
#         model = joblib.load(MODEL_FILE)
#         pipeline = joblib.load(PIPELINE_FILE)


# def predict(data: dict):
#     load_model()

#     df = pd.DataFrame([data])
#     transformed = pipeline.transform(df)
#     prediction = model.predict(transformed)

#     return float(prediction[0])


#or you can add below code - works same
import pandas as pd
from app.models.model_loader import load_model
from app.services.train_service import train_model
import os
from app.core.config import MODEL_PATH

def predict(data: dict):
    if not os.path.exists(MODEL_PATH):
        train_model()

    model, pipeline = load_model()

    df = pd.DataFrame([data])
    transformed = pipeline.transform(df)

    return float(model.predict(transformed)[0])