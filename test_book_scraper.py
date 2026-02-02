import unittest
import os
import csv
import logging
from book_scraper import OUTPUT_FILE

logging.basicConfig(
    level=logging.INFO,
    format="TEST | %(levelname)s | %(message)s"
)

class TestBookScraper(unittest.TestCase):
    def test_1_csv_file_download(self):
        self.assertTrue(os.path.exists(OUTPUT_FILE))
        logging.info("CSV file exists successfully")

    def test_2_csv_file_extraction(self):
        with open(OUTPUT_FILE, newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f))
        self.assertGreater(len(rows), 1)
        logging.info("CSV file contains data rows")

    def test_3_validate_file_type(self):
        self.assertTrue(OUTPUT_FILE.endswith(".csv"))
        logging.info("File format validated as CSV")

    def test_4_validate_data_structure(self):
        with open(OUTPUT_FILE, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)
        expected_headers = ["Title", "Price", "Rating", "Availability", "URL"]
        self.assertEqual(headers, expected_headers)
        logging.info("CSV headers validated successfully")

    def test_5_handle_missing_data(self):
        with open(OUTPUT_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for field, value in row.items():
                    self.assertTrue(value)
        logging.info("All rows contain valid data")

if __name__ == "__main__":
    unittest.main()
