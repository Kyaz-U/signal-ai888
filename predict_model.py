def predict_signal(last_3):
    avg = sum(last_3)/len(last_3)
    if avg >= 2.0:
        return 0.8
    elif avg >= 1.5:
        return 0.6
    else:
        return 0.3
