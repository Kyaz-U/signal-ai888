import requests

def get_latest_coefficients():
    url = "https://1win.games/aviator"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122",
        "Referer": "https://1win.com/",
        "X-Requested-With": "XMLHttpRequest"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        html = response.text
        import re
        matches = re.findall(r"(\d+\.\d+)x", html)
        coeffs = [float(x) for x in matches[:3]]
        if len(coeffs) == 3:
            return coeffs
        else:
            print("[XATO] Yetarli koeffitsiyent topilmadi")
            return [1.00, 1.00, 1.00]
    except Exception as e:
        print("[XATO] Scraperda xatolik:", e)
        return [1.00, 1.00, 1.00]
