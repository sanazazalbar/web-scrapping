# 📚 Book Data Web Scraper & Analysis (Python)

## 📌 Project Overview
Built a Python web scraper to extract book data from 
books.toscrape.com across 5 pages, collecting 100 books 
with title, price, and rating. Performed data analysis 
to uncover pricing trends and rating distribution.

## 🛠 Tools Used
- Python
- BeautifulSoup (web scraping)
- Requests (HTTP requests)
- CSV (data storage)

## 📊 Dataset — Real Numbers
| Metric | Value |
|---|---|
| Total Books Scraped | **100 books** |
| Pages Scraped | **5 pages** |
| Average Price | **£34.56** |
| Average Rating | **2.93 / 5** |
| Most Expensive Book | £58.11 |
| Cheapest Book | £10.16 |
| 5-Star Rated Books | **19 books** |

## 🔍 Analysis Performed
- **Average price** across 100 books — £34.56
- **Most expensive:** *The Death of Humanity* — £58.11
- **Cheapest:** *Patience* — £10.16
- **Rating distribution** across 5 levels (1 to 5 stars)
- **50 books** priced above average

## ⚙️ How It Works
1. Scraper loops through 5 pages with 1-second delay 
   between requests
2. Extracts title, price and star rating per book
3. Exports all 100 records to `all_books.csv`
4. Analysis script calculates avg price, avg rating, 
   most/least expensive books

## ▶️ How to Run
pip install beautifulsoup4 requests
python webscrapping.py   # scrapes data → all_books.csv
python Analysis.py       # runs analysis on CSV

## 💡 Skills Demonstrated
- Web scraping & HTTP request handling
- Data cleaning (price formatting, rating mapping)
- CSV data pipeline (collection → storage → analysis)
- Python loops, conditionals & file I/O

## 🚀 Conclusion
End-to-end data pipeline scraping 100 books across 
5 pages, storing structured data in CSV, and performing 
price & rating analysis using core Python — no external 
libraries required for analysis.
