from fastapi import FastAPI
from app.api.routes import router



def create_app():
    app = FastAPI(
        title="Housing Price Prediction API",
        version="1.0",
        description="ML API for predicting GGN housing prices"
    )

    # include routes
    app.include_router(router)

    return app


app = create_app()

@app.get("/health")
def health_check():
    return {"status": "ok"}