import requests
import re

def get_latest_coefficients():
    url = "https://1win.games/aviator"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122",
        "Referer": "https://1win.games/",
        "X-Requested-With": "XMLHttpRequest"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        html = response.text

        # log: faqat Railway logs'da ko‘rish uchun
        print("[HTML kesimi]:", html[:500])

        # regex orqali x.xx koeffitsiyentlarni qidirish
        matches = re.findall(r"(\\d+\\.\\d+)x", html)

        if matches and len(matches) >= 3:
            coeffs = [float(x) for x in matches[:3]]
            return coeffs
        else:
            print("[XATO] Koeffitsiyentlar topilmadi:", matches)
            return [1.0, 1.0, 1.0]

    except Exception as e:
        print("[XATO] API muammo:", e)
        return [1.0, 1.0, 1.0]
