#web scapper code
import requests
from bs4 import BeautifulSoup

response=requests.get('https://books.toscrape.com/')

value=BeautifulSoup(response.content,"html.parser")
books=value.find_all("article")
print(books)