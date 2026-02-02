Overview
This project is a Python-based web scraping application that collects book data from the “Books to Scrape” website.
The scraped data is saved into a CSV file so it can be used for analysis such as pricing trends, ratings, and stock availability

Website:
http://books.toscrape.com/

BUSINESS OBJECTIVE
The purpose of this project is to automate the process of collecting book information from an e-commerce website.
Manual data collection is time-consuming and error-prone. This solution provides clean, structured data for data analysis.

BUSINESS FLOW
→ Python Scraper
→ Data Validation
→ CSV File
→ Data Analysis

TECHNOLOGIES USED
Python
Requests (HTTP requests)
BeautifulSoup (HTML parsing)
CSV module (data storage)
Logging (error and process tracking)
Unittest (testing)

Project structure
book_scraper.py (main scraping file)
test_scraper.py (unit tests)
books_data.csv (output file)
README.txt

DATA COLLECTED
Each book contains the following information:
Title
Price
Rating (1 to 5)
Availability (In stock / Out of stock)
Product URL

HOW THE SCRAPER WORKS
Sends a request to the website
Parses the HTML page
Extracts book details from each page
Handles pagination automatically
Validates extracted data
Logs errors without stopping execution
Saves valid data to a CSV file

ERROR HANDLING
HTTP errors are logged
Books with missing fields are skipped
Network issues are handled safely
File writing errors are logged

TESTING
CSV file creation
Presence of data in CSV
File format correctness
Column structure validation
Handling of missing or invalid data
Tests are written using Python’s unittest module.
