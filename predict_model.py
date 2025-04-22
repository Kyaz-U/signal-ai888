import pickle
import numpy as np

def predict_signal(last_3):
    try:
        with open("models/aviator_model.pkl", "rb") as f:
            model = pickle.load(f)
        input_data = np.array(last_3).reshape(1, -1)
        probability = model.predict_proba(input_data)[0][1]  # ehtimol 1.80x+
        return probability
    except Exception as e:
        print("Xatolik modelni yuklashda:", e)
        return 0.0
