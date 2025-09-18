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
<link href="https://cdn.jsdelivr.net/gh/rastikerdar/iranyekan@v5.0.0/dist/font-face.css" rel="stylesheet" type="text/css"/>
<style>
body {{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    background: linear-gradient(135deg, #1e3a8a, #0f172a);
    font-family: 'IRANYekan', sans-serif;
    color: #00e6a8;
}}

.container {{
    text-align: center;
    background: rgba(255, 255, 255, 0.05);
    padding: 60px 100px;
    border-radius: 25px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.4);
}}

h1 {{
    font-size: 4rem;
    margin: 0;
}}

p {{
    font-size: 1.5rem;
    color: #a0f0c0;
    margin-top: 10px;
}}
</style>
</head>
<body>
<div class="container">
    <h1>{price_toman:,} تومان</h1>
    <p>قیمت دلار امروز</p>
</div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
