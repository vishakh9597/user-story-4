import requests
from bs4 import BeautifulSoup
import csv
import logging
from urllib.parse import urljoin

logging.basicConfig(
    level=logging.INFO,
    format="SCRAPER | %(levelname)s | %(message)s"
)

BASE_URL = "http://books.toscrape.com/"
OUTPUT_FILE = "books_data.csv"

def get_rating(rating_class):
    # convert rating into numbers
    rating_map = {
        "One": 1, "Two": 2, "Three": 3,
        "Four": 4, "Five": 5
    }
    rating = rating_map.get(rating_class, None)

    if rating is None:
        logging.warning(f"Unknown rating class encountered: {rating_class}")

    return rating

def scrape_books():
    #scrap books across all pages and store data in csv
    logging.info("Book scraping started")

    books = []
    url = BASE_URL
    page_count = 1

    while url:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"HTTP Error while accessing {url}: {e}")
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.select("article.product_pod")

        for index, book in enumerate(articles, start=1):
            try:
                title = book.h3.a["title"]
                price = book.select_one(".price_color").text.replace("£", "")
                availability = book.select_one(".availability").text.strip()
                rating_class = book.p["class"][1]
                rating = get_rating(rating_class)
                product_url = urljoin(url, book.h3.a["href"])

                if None in (title, price, rating, availability, product_url):
                    raise ValueError("Missing data field")

                books.append([
                    title, price, rating, availability, product_url
                ])
                logging.debug(f"Book {index} scraped successfully: {title}")

            except Exception as e:
                logging.warning(f"Skipping book {index} due to error: {e}")

# Handling of pagination
        next_page = soup.select_one("li.next a")
        if next_page:
            url = urljoin(url, next_page["href"])
            page_count += 1
        else:
            url = None

    logging.info(f"Total books scraped successfully: {len(books)}")
    save_to_csv(books)

def save_to_csv(data):
    #save data to csv file
    logging.info("Saving data to CSV file")

    try:
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price", "Rating", "Availability", "URL"])
            writer.writerows(data)

        logging.info(f"CSV file '{OUTPUT_FILE}' saved successfully")

    except Exception as e:
        logging.error(f"Error while saving CSV file: {e}")

if __name__ == "__main__":
    logging.info("Scraper execution started")
    scrape_books()
    logging.info("Scraper execution finished")
