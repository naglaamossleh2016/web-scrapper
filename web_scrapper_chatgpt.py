# I asked chatgpt to refactor code in web_scrapper.py and documented it
# Here is the code
import requests
from bs4 import BeautifulSoup

def scrape_books_data(url):
    """
    Scrape book data from a given URL.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        list: A list of dictionaries containing book information.
    """
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the book articles on the page
        books = soup.find_all("article")

        # Initialize an empty list to store book information
        book_data_list = []

        # Iterate through each book article
        for book in books:
            # Extract book title from the anchor tag within the h3 tag
            title = book.h3.a["title"]

            # Extract the rating from the class attribute of the p tag
            rating = book.p["class"][1]

            # Extract the price from the p tag with class "price_color"
            price = book.select_one("p.price_color").get_text(strip=True)

            # Create a dictionary to store the book information
            book_data = {
                "title": title,
                "rating": rating,
                "price": price
            }

            # Add the book information to the list
            book_data_list.append(book_data)

            # Print the book information
            print(f"Book title: {title} ***** Rating: ({rating}) stars $$$$$ Price: {price}")

        # Return the list of book information
        return book_data_list
    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch data from {url}")
        return []

# URL of the website to scrape
url = 'https://books.toscrape.com/'

# Call the function to scrape book data and store the result in a variable
scraped_books = scrape_books_data(url)
