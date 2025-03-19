import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd

# I use headers to avoid getting blocked by the website
def get_journals(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}):
    response = requests.get(url, headers=headers)
    # Check if the page is successfully retrieved
    if response.status_code != 200:
        print(f"Failed to retrieve page: {url}")
        return []

    soup = BeautifulSoup(response.text, "lxml")
    bookdata = []
    # Find all data that i need from the page
    for i in soup.find_all("div", class_="results_bio"):
        title = i.find("a", class_="hideIE")
        author = i.find("div", class_="displayElementText highlightMe AUTHOR")
        call_number = i.find("div", class_="displayElementText highlightMe PREFERRED_CALLNUMBER")
        status = i.find("div", class_="displayElementText highlightMe PARENT_AVAILABLE")
    # Append the data to the list
        bookdata.append({
            "Title": title.text.strip() if title else "No Title",
            "Author": author.text.strip() if author else "No Author",
            "Call Number": call_number.text.strip() if call_number else "No Call Number",
            "Status": status.text.strip() if status else "No Status"
        })

    return bookdata

# Get all books from the library
def get_total_books(amount_books):
    bookdata = []
    base_url = "https://katalog.hacettepe.edu.tr/client/tr_TR/default_tr/search/results?rw={}&te=ILS&isd=true"

    for i in range(0, amount_books, 12):  # Assuming 12 results per page
        url = base_url.format(i)
        print(f"Scraping: {url}")
        print(f"Progress: {i}/{amount_books}")
        print(f"{i/amount_books*100:.2f}% completed") 
        bookdata.extend(get_journals(url))

    return bookdata



total_books = get_total_books(374747)  # Fetch 374747 books (this is the total number of books in the library)
# Create a dataframe
df = pd.DataFrame(total_books)
# Save the data to an excel file
df.to_excel("library_books.xlsx", index=False, engine='openpyxl')

print("Scraping completed. Data saved to 'library_books.xlsx'.")
