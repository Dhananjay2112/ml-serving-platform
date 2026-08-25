"""
FastAPI serving layer for the trained model.

Loads the latest registered MLflow model on startup and exposes:
  GET  /health   - liveness/readiness probe target
  POST /predict  - single prediction endpoint
  GET  /metrics  - Prometheus metrics (request count, latency, prediction distribution)
"""
import os
import time

import mlflow.pyfunc
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

MODEL_URI = os.getenv("MODEL_URI", "models:/serving-model/Production")

app = FastAPI(title="Model Serving API")

REQUEST_COUNT = Counter("predict_requests_total", "Total prediction requests")
REQUEST_LATENCY = Histogram("predict_latency_seconds", "Prediction latency")
PREDICTION_DIST = Counter("predictions_by_class_total", "Predictions by class", ["predicted_class"])

model = None


class PredictRequest(BaseModel):
    features: list[float]


@app.on_event("startup")
def load_model():
    global model
    model = mlflow.pyfunc.load_model(MODEL_URI)


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


@app.post("/predict")
def predict(req: PredictRequest):
    REQUEST_COUNT.inc()
    start = time.time()

    prediction = model.predict([req.features])[0]

    REQUEST_LATENCY.observe(time.time() - start)
    PREDICTION_DIST.labels(predicted_class=str(prediction)).inc()

    return {"prediction": str(prediction)}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
