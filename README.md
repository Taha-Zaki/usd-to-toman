# 💵 USD to Toman Live Dashboard

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Taha-Zaki/usd-to-toman/main.yml?branch=main&label=Build&logo=github)
![GitHub Pages](https://img.shields.io/github/deployments/Taha-Zaki/usd-to-toman/github-pages?logo=github)

یک صفحه‌ی ساده، زیبا و **ریسپانسیو** که قیمت دلار به تومان را به‌صورت آنلاین نمایش می‌دهد. این پروژه از **Python + GitHub Actions + GitHub Pages** استفاده می‌کند و هر ۳۰ دقیقه قیمت را به‌روزرسانی می‌کند.

---

## 🚀 ویژگی‌ها

* دریافت نرخ دلار از سایت [TGJU](https://www.tgju.org/dollar-chart)
* تبدیل به تومان
* طراحی زیبا و مینیمال با **فونت ایران یکان**
* ریسپانسیو برای موبایل و دسکتاپ
* بروزرسانی خودکار با **GitHub Actions**
* میزبانی رایگان روی **GitHub Pages**

---

## 🛠️ نصب و اجرا (Local)

1. کلون کردن مخزن:

```bash
git clone https://github.com/Taha-Zaki/usd-to-toman.git
cd usd-to-toman
```

2. نصب پیش‌نیازها:

```bash
pip install -r requirements.txt
```

3. اجرای اسکریپت:

```bash
python update_price.py
```

4. فایل `index.html` در همان مسیر ایجاد می‌شود و می‌توانید با مرورگر باز کنید.

---

## ⏱️ آپدیت خودکار با GitHub Actions

* اکشن هر **۳۰ دقیقه** اجرا می‌شود و قیمت دلار را می‌گیرد
* فایل `index.html` را در branch اصلی push می‌کند
* سایت شما روی GitHub Pages به‌روز می‌ماند

> مسیر GitHub Pages: [https://Taha-Zaki.github.io/usd-to-toman/](https://Taha-Zaki.github.io/usd-to-toman/)

---

## 📁 ساختار پروژه

```
usd-to-toman/
├── update_price.py       # اسکریپت اصلی پایتون
├── index.html            # فایل HTML خروجی
├── requirements.txt      # پیش‌نیازهای پایتون
└── .github/
    └── workflows/
        └── main.yml   # اکشن GitHub
```

---

## 🎨 طراحی و ظاهر

* پس‌زمینه گرادینت آبی تیره تا مشکی
* کارت شیشه‌ای نیمه‌شفاف با سایه و گوشه‌های گرد
* قیمت دلار بزرگ و وسط صفحه
* متن توضیحی زیر قیمت با رنگ ملایم
* ریسپانسیو برای تمامی اندازه‌ها

---

## 🔗 منابع

* [TGJU - دلار](https://www.tgju.org/dollar-chart)
* [Iran Yekan Font](https://rastikerdar.github.io/iranyekan/)
* [GitHub Pages](https://pages.github.com/)
* [GitHub Actions](https://docs.github.com/en/actions)

---

## ⚡ نکات حرفه‌ای

* برای تغییر زمان آپدیت، فایل اکشن `.github/workflows/main.yml` را ویرایش کنید
* می‌توانید استایل و رنگ‌ها را در `update_price.py` تغییر دهید
* پروژه کاملاً رایگان و متن‌باز است




https://taha-zaki.github.io/usd-to-toman/data.json
