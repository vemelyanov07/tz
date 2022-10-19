import requests
from bs4 import BeautifulSoup
import lxml
import json


url = "https://oriencoop.cl/sucursales.htm"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
req = requests.get(url, headers=headers)
src = req.text
# print(src)

soup = BeautifulSoup(src, 'lxml')

all_categories_dict = []
table_head = soup.find(class_ = "s-dato").find('p').find_all('span')

for item in table_head:
    product_tds = item.find_all("span")

    # address = table_head[0].find("p").text
    address = table_head[0].text
    latlon = table_head[0].text
    name = table_head[0].text
    phones = table_head[0].text
    working_hours = table_head[0].text

    # print(address)

    all_categories_dict.append(
        {
            "address" : address,
            "latlon" : latlon,
            "name" : name,
            "phones" : phones,
            "working_hours" : working_hours
        }
    )

# # print(table_head)

with open('all_categories_dict.json', 'w', encoding='utf-8') as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

# with open('index.html', "a", encoding='utf-8') as file:
#     file.write(src)


# with open('index.html', encoding='utf-8') as file:
#     src = file.read()

# all_categories_dict = {}
# soup = BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_='sub-menu')
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://oriencoop.cl"+ str(item.get("href"))
#     # print(f'{item.text}:{item_href}')
#     all_categories_dict[item_text] = item_href


# with open('all_categories_dict.json', 'w', encoding='utf-8') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

# with open('all_categories_dict.json', encoding='utf-8') as file:
#     all_categories = json.load(file)






    