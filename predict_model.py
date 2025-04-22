import pickle
import numpy as np

def predict_signal(last_3):
    with open("models/aviator_model.pkl", "rb") as f:
        model = pickle.load(f)
    input_data = np.array(last_3).reshape(1, -1)
    return model.predict_proba(input_data)[0][1]  # Ehtimol: 1.80x+
