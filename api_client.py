import pandas as pd

def get_latest_coefficients():
    df = pd.read_csv("data/aviator.csv")
    last_row = df.iloc[-1]
    return [last_row['k1'], last_row['k2'], last_row['k3']]
