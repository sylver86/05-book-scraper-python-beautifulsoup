import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
from urllib.parse import urljoin
import re
import os

# --- Configurazione del Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

def fetch_html(url: str) -> BeautifulSoup | None:
    """
    Effettua una richiesta GET all'URL specificato e restituisce un oggetto BeautifulSoup.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, "lxml")
    except requests.exceptions.RequestException as e:
        logging.error(f"Errore durante la richiesta HTTP per {url}: {e}")
        return None

def parse_book_details(book_soup: BeautifulSoup) -> dict:
    """
    Estrae i dettagli di un singolo libro da un tag <article> di BeautifulSoup.
    """
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    title_tag = book_soup.find("h3").find("a")
    title = title_tag["title"] if title_tag else "Title not found"

    rating_tag = book_soup.find("p", class_="star-rating")
    rating_class = rating_tag["class"][1] if rating_tag and len(rating_tag.get("class", [])) > 1 else None
    rating = rating_map.get(rating_class, 0)

    price_tag = book_soup.find("p", class_="price_color")
    price_str = price_tag.text if price_tag else "£0.00"
    price_match = re.search(r'[\d\.]+', price_str)
    price_float = float(price_match.group(0)) if price_match else 0.0

    availability_tag = book_soup.find("p", class_="instock availability")
    availability = availability_tag.text.strip() if availability_tag else "Availability not found"

    return {
        "Title": title,
        "Rating": rating,
        "Price_Pounds": price_float,
        "Availability": availability
    }

def get_next_page_url(soup: BeautifulSoup, base_url: str) -> str | None:
    """
    Trova l'URL della pagina successiva, se esiste, e lo costruisce correttamente.
    """
    next_page_tag = soup.select_one("li.next > a")
    if next_page_tag:
        relative_url = next_page_tag["href"]
        return urljoin(base_url, relative_url)
    return None

def scrape_all_books(start_url: str) -> pd.DataFrame:
    """
    Orchestra l'intero processo di scraping, navigando tra le pagine.
    """
    all_books_data = []
    current_url = start_url
    page_count = 1

    while current_url:
        logging.info(f"Scraping pagina {page_count}: {current_url}")
        soup = fetch_html(current_url)

        if not soup:
            logging.warning(f"Impossibile recuperare la pagina {current_url}. Interruzione dello scraping.")
            break

        books_on_page = soup.find_all("article", class_="product_pod")
        if not books_on_page:
            logging.warning(f"Nessun libro trovato sulla pagina {current_url}. Potrebbe essere cambiata la struttura del sito.")
            break

        for book_soup in books_on_page:
            book_data = parse_book_details(book_soup)
            all_books_data.append(book_data)

        current_url = get_next_page_url(soup, current_url)
        page_count += 1

    logging.info(f"Scraping completato. Estratti dati da {page_count - 1} pagine.")
    return pd.DataFrame(all_books_data)

# --- Blocco di Esecuzione Principale ---
if __name__ == '__main__':
    BASE_URL = "https://books.toscrape.com/catalogue/page-1.html"
    OUTPUT_FILE = "books_data.csv"

    logging.info("Avvio dello script di web scraping.")

    books_df = scrape_all_books(BASE_URL)

    if not books_df.empty:
        logging.info(f"Totale libri estratti: {len(books_df)}")
        print("\nAnteprima dei dati estratti:")
        print(books_df.head())

        try:
            books_df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
            logging.info(f"Dati salvati con successo in '{os.path.abspath(OUTPUT_FILE)}'")
        except IOError as e:
            logging.error(f"Errore durante il salvataggio del file CSV: {e}")
    else:
        logging.warning("Nessun dato è stato estratto, il file CSV non sarà creato.")

    logging.info("Esecuzione dello script terminata.")
