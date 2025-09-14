# 🕷️ Web Scraping & Product Display App

Welcome to the **Web Scraping Product Display** project! This is a full-stack application built with **Scrapy**, **Django**, and **React**. It scrapes product data from an e-commerce website and displays it in a user-friendly frontend interface.

---

## 🚀 Project Overview

- 🐍 **Backend**: Django + Django REST Framework
- ⚛️ **Frontend**: React.js
- 🕸️ **Scraper**: Scrapy (Python Web Crawler)
- 🗂 **Data Format**: JSON

---

## 🗂️ Project Structure


📁 web_scraping/
│
├── 📦 product_api/ # Django backend
│ └── manage.py # Django manager
│
├── 📦 product_frontend/ # React frontend
│ └── src/App.js # Main React app
│
├── 📦 my_new_scrapy_project/
│ └── my_new_scrapy_project/
│ ├── spiders/
│ │ ├── nobero_spider.py # Scrapy spider
│ │ └── output1.json # Scraped JSON data



---

## ⚙️ Running the Project

### 🐍 Django Setup

Navigate to the Django backend directory:




## Screenshots
<img src="react front end 2.png" alt="Frontend Screenshot" width="800">
<img src="django rest framework screenshot 2.png" alt="Frontend Screenshot" width="800">

```bash
cd D:\intern\web_scrapping\scrap\scrap\spiders\scrapper\django\product_api


---

## ⚙️ Running the Project

### 🐍 Django Setup

Navigate to the Django backend directory:


cd D:\intern\web_scrapping\scrap\scrap\spiders\scrapper\django\product_api

python manage.py runserver


⚛️ React Setup
Navigate to the React frontend directory:


cd D:\intern\web_scrapping\scrap\scrap\spiders\scrapper\product_frontend\src
Start the React development server:


npm start
Make sure both Django and React are running simultaneously to see the full application in action.



🕸️ Scrapy Configuration
📍 Scraped Data Location:
Your scraped JSON data is saved here:

makefile
D:\intern\web_scraping\scrap\my_new_scrapy_project\my_new_scrapy_project\spiders\output1.json
🕷️ Spider File:
makefile

D:\intern\web_scraping\scrap\my_new_scrapy_project\my_new_scrapy_project\spiders\nobero_spider.py


📥 Importing Scraped Data into Django
If the JSON file hasn't been imported yet, use the following command:


python manage.py load_products D:\intern\web_scraping\scrap\my_new_scrapy_project\my_new_scrapy_project\spiders\output1.json


📦 Dependencies
Ensure the following are installed and configured properly:

Python 3.x

Django & Django REST Framework

Scrapy

Node.js & npm

React

Install Python dependencies:


pip install -r requirements.txt
Install Node dependencies:


npm install





