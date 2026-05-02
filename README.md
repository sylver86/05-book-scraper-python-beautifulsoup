# Book Scraper — Python Web Scraping Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Parsing-green)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Export-150458?logo=pandas&logoColor=white)

## Overview

Web scraper that crawls all 50 pages of [books.toscrape.com](http://books.toscrape.com), extracts structured data for every book in the catalogue, and exports a clean CSV — 1,000 books total.

Demonstrates a production-style scraping pipeline: modular single-responsibility functions, structured logging, robust error handling for network and parsing failures, and dependency isolation via `venv`.

---

## Output

| Field | Type | Example |
|-------|------|---------|
| title | string | "A Light in the Attic" |
| price | float (£) | 51.77 |
| star_rating | int (1–5) | 3 |
| availability | string | "In stock" |

Output: `books_data.csv` — 1,000 rows, one per book.

---

## Features

- Crawls all 50 pages automatically via pagination detection
- Structured logging: per-page progress and error events
- Graceful error handling for network timeouts and parsing failures
- `lxml` parser for fast, reliable HTML parsing

---

## Setup

```bash
git clone https://github.com/sylver86/05-book-scraper-python-beautifulsoup.git
cd 05-book-scraper-python-beautifulsoup

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

```bash
python src/scraper.py
```

`books_data.csv` is written to the project root on completion.

---

## Code Structure

```
05-book-scraper-python-beautifulsoup/
├── src/
│   └── scraper.py      # fetch_html · parse_page · handle_pagination · export_csv
├── requirements.txt
└── README.md
```

---

## Technologies

`Python 3.10+` · `requests` · `BeautifulSoup4` · `lxml` · `pandas`
