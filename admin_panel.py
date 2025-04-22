import os
import csv

def get_statistics():
    log_path = "logs/signals.csv"
    if not os.path.exists(log_path):
        return "Hali signal log mavjud emas."

    with open(log_path, "r") as f:
        reader = list(csv.reader(f))
        total = len(reader)
        last = reader[-1] if total > 0 else None

    result = f"🔧 Statistika:\nJami signal: {total}\n"
    if last:
        result += f"So‘nggi signal: {last[0]} ➜ {last[2]}% ({last[1]})"
    return result
