# update_price.py
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def fetch_usd_irr():
    url = "https://www.tgju.org/dollar-chart"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=15)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    td = soup.find("td", class_="nf")
    if td is None:
        raise RuntimeError("Couldn't find price element on page")
    text = td.get_text(strip=True)
    digits = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")
    translated = text.translate(digits)
    numeric = ''.join(filter(str.isdigit, translated))
    if not numeric:
        raise RuntimeError(f"No digits found in extracted text: {text!r}")
    number = int(numeric)
    return number

def build_html(price_toman):
    return f"""<!DOCTYPE html>
<html lang="fa">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>قیمت دلار</title>
<style>
body{{font-family:sans-serif;display:flex;align-items:center;justify-content:center;height:100vh;background:#0f172a;color:#00e6a8}}
.container{{text-align:center}}
h1{{font-size:3rem;margin:0}}
p{{opacity:.8}}
</style>
</head>
<body>
  <div class="container">
    <h1>{price_toman:,} تومان</h1>
    <p>قیمت دلار لحظه‌ای</p>
  </div>
</body>
</html>"""

def main():
    price_irr = fetch_usd_irr()
    price_toman = price_irr // 10
    now_iso = datetime.utcnow().isoformat() + "Z"

    # تولید HTML
    html = build_html(price_toman)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    # تولید JSON
    data = {
        "usd_price_irr": price_irr,
        "usd_price_toman": price_toman,
        "currency": "IRR",
        "source": "tgju.org",
        "fetched_at_utc": now_iso,
        "status": "success"
    }
    with open("data.json", "w", encoding="utf-8") as jf:
        json.dump(data, jf, ensure_ascii=False, indent=2)

    print("Updated index.html and data.json")

if __name__ == "__main__":
    main()
