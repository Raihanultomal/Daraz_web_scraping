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

        try:
            price = details_soup.find('td', class_ = "product-info-data product-price").text.replace('৳', '')
        except:
            price = ""
        # print(price)

        try:
            regular_price = details_soup.find('td', class_ = "product-info-data product-regular-price").text.replace('৳', '')
        except:
            regular_price = ""
        # print(regular_price)

        try:
            status = details_soup.find('td', class_ = "product-info-data product-status").text
        except:
            status = ""
        # print(status)

        try:
            product_code = details_soup.find('td', class_ = "product-info-data product-code").text
        except:
            product_code = ""
        # print(product_code)

        try:
            product_brand = details_soup.find('td', class_ = "product-info-data product-brand").text
        except:
            product_brand = ""
        # print(product_brand)

        try:
            key_feature = details_soup.find('div', class_ = "short-description").ul.text.replace('View More Info','')
        except:
            key_feature = ""    

        # print(key_feature)


        # key_feature = details_soup.find('div', class_ = "short-description").ul.text.replace('View More Info','')
        # print(key_feature)
        # print("\n")

        try:
            description = details_soup.find('div', class_ = "full-description").text
        except:
            description = ""
        # print(description)

        

        product = {
            'Product Name' : title,
            'Product Price': price,
            'Regular Price': regular_price,
            'Product Status': status,
            'Product Code' : product_code,
            'Brand' : product_brand,
            'Key Feature' : key_feature,
            'Description' : description,
        }
        product_list.append(product)

    return


def page(soup):
    divs = soup.find_all('div', class_ = "p-item")
    try:
        page = soup.find('div', class_ = "col-md-6 rs-none text-right").p.text.split("(")[-1].replace(' Pages)','')
    except:
        page = ""
    return page


p = laptop(1)
pg = int(page(p))

product_list = []
# print(len(product_list))


print(f"The nnumber of total page is {pg} ")

for i in range(1,pg):
    print(f'Scraping page {i}.........!')
    c = laptop(i)
    extract(c)


df = pd.DataFrame(product_list)
df.to_csv('Products.csv')



# p-item-img
# p-item
