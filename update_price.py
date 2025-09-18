import requests
from bs4 import BeautifulSoup

def fetch_usd_irr():
    url = "https://www.tgju.org/dollar-chart"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=15)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    td = soup.find("td", class_="nf")
    text = td.get_text(strip=True)
    digits = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")
    number = int(''.join(filter(str.isdigit, text.translate(digits))))
    return number

price_irr = fetch_usd_irr()
price_toman = price_irr // 10

html_content = f"""
<!DOCTYPE html>
<html lang="fa">
<head>
<meta charset="UTF-8">
<title>قیمت دلار</title>
<style>
body {{
    display: flex; justify-content: center; align-items: center;
    height: 100vh; background: #0f172a; color: #00e6a8;
    font-family: sans-serif; font-size: 50px;
}}
</style>
</head>
<body>
قیمت دلار: {price_toman} تومان
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
