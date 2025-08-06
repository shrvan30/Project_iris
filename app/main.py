from fastapi import FastAPI, HTTPException
from joblib import load
import numpy as np
from app.schemas import IrisRequest, IrisResponse
import pickle

app = FastAPI(title="Iris Classifier API")

# The Model is Loaded Here in Api code
try:
    with open("model/iris_model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

# Class label map with repective species
species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}

@app.get("/")
def root():
    return {"message": "Iris Classifier API is running."}

@app.post("/predict", response_model=IrisResponse)
def predict_species(data: IrisRequest):
    try:
        X = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
        prediction = model.predict(X)[0]
        return {"species": species_map[prediction]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")
