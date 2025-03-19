# Library Book Scraper

This project is a Python-based web scraper designed to collect book data from the Hacettepe University Library catalog. The scraper retrieves book details such as title, author, call number, and location, then stores the data in an Excel file.

## Features
- Scrapes book details from the Hacettepe University library catalog
- Extracts:
  - Title
  - Author
  - Call Number
  - Location
- Saves the extracted data into an Excel file (`library_books.xlsx`)
- Uses `requests` and `BeautifulSoup` to fetch and parse HTML data
- Implements headers to prevent blocking

## Requirements
Ensure you have the following dependencies installed before running the script:
```bash
pip install requests beautifulsoup4 lxml pandas openpyxl
```

## Usage
Run the script using:
```bash
python main.py
```
This will scrape the library's book data and save it in an Excel file.

## Data Collection Limitations
The library has approximately **374,747** books, but due to server constraints, only **150,000** books were successfully scraped. The server did not support excessive requests, causing partial data collection.

## File Structure
```
├── .venv/  # Virtual environment (optional)
├── __pycache__/  # Compiled Python files
├── library_books.xlsx  # Output Excel file with scraped book data
├── main.py  # Main scraping script
├── README.md  # Project documentation
```

## Notes
- The scraper makes multiple paginated requests (12 results per page).
- Excessive requests may lead to temporary IP bans.
- Modify the `amount_books` variable in `main.py` to adjust the number of books fetched.

## Disclaimer
This scraper is for educational purposes only. Ensure compliance with the website's terms of service before scraping.

