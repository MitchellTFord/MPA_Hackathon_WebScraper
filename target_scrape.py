import requests
from bs4 import BeautifulSoup

url = "https://www.target.com/s?searchTerm=toilet+paper"
headers = {'user-agent': 'my-app/0.0.1'}
result = requests.get(url, headers=headers)
html = result.content

soup = BeautifulSoup(html, 'lxml')

divs = soup.find_all('div')

#productCards = soup.find_all('svg')
productCards = soup.find_all('div', {'data-test' : "product-card-default"})

print(len(productCards))