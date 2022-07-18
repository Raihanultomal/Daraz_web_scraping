import requests

from bs4 import BeautifulSoup

import pandas as pd


def laptop(page):
    url = f"https://www.startech.com.bd/laptop-notebook/laptop?page={page}"
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup
def extract(soup):
    # divs = soup.find_all('div',class_ = "p-item-img")
    divs = soup.find_all('div', class_ = "p-item")

    for links in divs:

        collect_links = links.a['href']
        # print(collect_links)

        details_url = collect_links
        details_r = requests.get(details_url)
        details_soup = BeautifulSoup(details_r.content, 'lxml')
        title = details_soup.find('h1', class_ = "product-name").text
        # print(title)

        price = details_soup.find('td', class_ = "product-info-data product-price").text.replace('৳', '')
        # print(price)

        regular_price = details_soup.find('td', class_ = "product-info-data product-regular-price").text.replace('৳', '')
        # print(regular_price)

        status = details_soup.find('td', class_ = "product-info-data product-status").text
        # print(status)

        product_code = details_soup.find('td', class_ = "product-info-data product-code").text
        # print(product_code)

        product_brand = details_soup.find('td', class_ = "product-info-data product-brand").text
        # print(product_brand)

        try:
            key_feature = details_soup.find('div', class_ = "short-description").ul.text.replace('View More Info','')
        except:
            key_feature = ""    

        # print(key_feature)


        # key_feature = details_soup.find('div', class_ = "short-description").ul.text.replace('View More Info','')
        # print(key_feature)
        # print("\n")

        description = details_soup.find('div', class_ = "full-description").text
        # print(description)

        product = {
            'Product Name' : title,
            'Product Price': price,
            'Regular Price': regular_price,
            'Product Status': status,
            'Product Code' : product_code,
            'Brand' : product_brand,
            'Key Feature' : key_feature,
        }
        product_list.append(product)
    return
        

product_list = []
# print(len(product_list))

print("Enter the number of page")
x = input()
for i in range(1,int(x)):
    print(f'Scraping page {i}.........!')
    c = laptop(i)
    extract(c)


df = pd.DataFrame(product_list)
df.to_csv('Product.csv')



# p-item-img
# p-item
