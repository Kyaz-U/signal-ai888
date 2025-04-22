import csv
import os
from datetime import datetime

def log_signal(coefficients, probability):
    os.makedirs("logs", exist_ok=True)
    file_path = "logs/signals.csv"
    with open(file_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), coefficients, round(probability * 100, 2)])
