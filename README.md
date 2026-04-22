# Project Name: Daraz Product Web Scraper

### 1. Project Overview
* **Target Website:** https://www.daraz.pk/
* **Data Fields Extracted:** Product Name, Price
* **Tools Used:** Python, Selenium, Pandas

### 2. Setup Instructions
1. Clone this repo: `git clone https://github.com/mini-crypto/web-scraper-daraz.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run script: `python scraper.py`

### 3. How It Works
This project uses Selenium to automate a browser. It searches for products on Daraz, extracts product names and prices, and stores the data into a CSV file using Pandas.

### 4. Challenges & Solutions
* Daraz is a dynamic website where content loads using JavaScript. Initially, BeautifulSoup could not extract the data. This problem was solved by using Selenium, which allows interaction with dynamically loaded content.

### 5. Output
The extracted data is saved in a file named `data.csv`.
### 5. Ethical Note
This scraper respects website loading time using delays and avoids excessive requests to prevent server overload.
