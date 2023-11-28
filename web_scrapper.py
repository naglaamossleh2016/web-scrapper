#web scapper code
import requests
from bs4 import BeautifulSoup

response=requests.get('https://books.toscrape.com/')

value=BeautifulSoup(response.content,"html.parser")
books=value.find_all("article")
print(books[0])
for book in books:
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    price = book.select_one("p.price_color").get_text(strip=True)
    print(f"Book title: {title} ***** rating: ({rating}) stars $$$$$ price: {price}")