import requests

from bs4 import BeautifulSoup



def phone(page):
    url = 'https://www.daraz.com.bd/smartphones/?page={page}'
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def extract(soup):
    divs = soup.find_all('div', class_ = 'box--pRqdD')
    return len(divs)

c = phone(1)

print(extract(c))
