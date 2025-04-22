import pickle
import numpy as np

def predict_signal(k1, k2, k3):
    with open("models/aviator_model.pkl", "rb") as file:
        model = pickle.load(file)
    
    X = np.array([[k1, k2, k3]])
    probability = model.predict_proba(X)
    return float(probability[0][1])  # 1.80x+ ehtimoli
