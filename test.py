import requests
from bs4 import BeautifulSoup

url = 'https://www.adwdiabetes.com/catalog/diabetic-test-strips_54.htm'

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

gen = soup.find_all('tr', {'id': 'prdtblclr'})
print(gen)
count = 0
for item in gen:
    count += 1
    # Dealer Name
    # website = 'Walgreens'
    #
    #
    # # Gets the product name
    # name = item.find_all('h2', {'class': 'product-name'})[0].text.strip()
    #
    #
    # manufacturer = item.find_all('h2', {'class': 'product-name'})[0].text.strip().split()[0]
    #
    #
    # # Get Product Link
    # href = item.find_all('a')[0].get('href')
    #
    #
    # # Get Product Price
    # price = item.find_all('p', {'class': 'special-price'})[0].text.strip()
    #
    #
    # # type of protein
    # prod_type = "Test Strips"
    #
    #
    # # Product Image
    # image = item.find_all('img')[0].get('data-src')
    #
    #
    # # product promos
    # promo = item.find_all('div', {'class': 'promo-text'})[0].text.strip()
    #
    #
    # # Per Serving

print(count)
