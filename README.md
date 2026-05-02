# BookHarvest — Pipeline di Web Scraping Professionale

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-HTML%20Parsing-green)
![Pandas](https://img.shields.io/badge/Pandas-Export%20CSV-150458?logo=pandas&logoColor=white)
![requests](https://img.shields.io/badge/requests-HTTP-blue)

## Panoramica

Pipeline di web scraping che crawla le 50 pagine del catalogo [books.toscrape.com](http://books.toscrape.com), estrae dati strutturati per 1.000 libri e produce un CSV pulito. Il progetto dimostra un approccio professionale alla raccolta dati: funzioni single-responsibility, logging strutturato, gestione robusta degli errori e isolamento delle dipendenze.

Competenza applicabile in progetti enterprise di data collection da sorgenti web, arricchimento dati di prodotto, price intelligence e integrazione di fonti dati eterogenee.

## Valore Enterprise

| Settore / Azienda | Rilevanza |
|-------------------|-----------|
| Retail & E-commerce | Price monitoring, product data enrichment, competitive intelligence |
| IT Consulting (Accenture, NTT Data) | Data collection da sorgenti esterne come fase di pipeline ETL |
| Data Reply / Engineering | Integrazione scraper in workflow di ingestione dati enterprise |
| Qualsiasi settore | Raccolta dati strutturati da sorgenti web non-API |

## Output

| Campo | Tipo | Esempio |
|-------|------|---------|
| `title` | string | "A Light in the Attic" |
| `price` | float (£) | 51.77 |
| `star_rating` | int (1–5) | 3 |
| `availability` | string | "In stock" |

Output finale: `books_data.csv` — 1.000 righe, una per libro.

## Caratteristiche

- Crawling automatico di tutte le 50 pagine tramite rilevamento paginazione
- Logging strutturato: progresso per pagina ed eventi di errore
- Gestione errori: timeout di rete, fallimenti di parsing
- Parser `lxml` per analisi HTML veloce e affidabile

## Setup

```bash
git clone https://github.com/sylver86/05-book-scraper-python-beautifulsoup.git
cd 05-book-scraper-python-beautifulsoup

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python src/scraper.py
```

## Struttura Repository

```
05-book-scraper-python-beautifulsoup/
├── src/
│   └── scraper.py       # fetch_html · parse_page · handle_pagination · export_csv
├── requirements.txt
├── LICENSE
└── README.md
```

## Stack Tecnologico

`Python 3.10+` · `requests` · `BeautifulSoup4` · `lxml` · `pandas`

---

---

# BookHarvest — Professional Web Scraping Pipeline 🇬🇧

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-HTML%20Parsing-green)

## Overview

Web scraping pipeline that crawls all 50 pages of [books.toscrape.com](http://books.toscrape.com), extracts structured data for 1,000 books, and produces a clean CSV. Demonstrates a production-style approach: single-responsibility functions, structured logging, robust error handling, and dependency isolation.

## Output

| Field | Type | Example |
|-------|------|---------|
| `title` | string | "A Light in the Attic" |
| `price` | float (£) | 51.77 |
| `star_rating` | int (1–5) | 3 |
| `availability` | string | "In stock" |

Output: `books_data.csv` — 1,000 rows, one per book.

## Features

- Automatic pagination crawling across all 50 pages
- Structured logging: per-page progress and error events
- Graceful error handling: network timeouts, parsing failures
- `lxml` parser for fast, reliable HTML parsing

## Setup

```bash
git clone https://github.com/sylver86/05-book-scraper-python-beautifulsoup.git
cd 05-book-scraper-python-beautifulsoup

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python src/scraper.py
```

## Project Structure

```
05-book-scraper-python-beautifulsoup/
├── src/
│   └── scraper.py       # fetch_html · parse_page · handle_pagination · export_csv
├── requirements.txt
├── LICENSE
└── README.md
```

## Technologies

`Python 3.10+` · `requests` · `BeautifulSoup4` · `lxml` · `pandas`
