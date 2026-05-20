import requests
from bs4 import BeautifulSoup

print("--- Mini Challenge 1: The Book Scraper ---")

# 1. The Target URL
url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

# 2. Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 3. Find all the book containers
# TODO: Inspect the website and find the correct tag and class for the books
books = soup.find_all("article", class_="product_pod")

print(f"Found {len(books)} books! Extracting data...\n")

for book in books:
    # TODO: Extract the title. (Hint: look inside the <h3> and <a> tags)
    title = "YOUR_CODE_HERE" 
    
    # TODO: Extract the price. (Hint: look for a <p> tag with the class 'price_color')
    price = "YOUR_CODE_HERE"
    
    print(f"📖 Title: {title} | 💰 Price: {price}")