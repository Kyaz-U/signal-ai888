import pandas as pd
import numpy as np
import pickle
import os

MODEL_PATH = "models/aviator_model.pkl"

def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

def predict_signal(k1, k2, k3):
    model = load_model()
    input_data = pd.DataFrame([[k1, k2, k3]], columns=["k1", "k2", "k3"])
    probability = model.predict_proba(input_data)[0][1]
    return round(probability * 100, 2)
