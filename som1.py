import requests
from bs4 import BeautifulSoup
import lxml
import json


url = "https://som1.ru/shops/"
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
req = requests.get(url, headers=headers)
src = req.text
# print(src)

soup = BeautifulSoup(src, 'lxml')

all_city_dict = []
city_head = soup.find(class_ = "col-xs-12 itjCitys").find("input").find_all('label')

for item in city_head:
    product_tds = item.find_all("label")
    # print(product_tds)

    # address = table_head[0].find("p").text
    address = city_head[0].text
    latlon = city_head[1].text
    name = city_head[2].text
    phones = city_head[3].text
    working_hours = city_head[4].text

    # print(address)

    all_city_dict.append(
        {
            "address" : address,
            "latlon" : latlon,
            "name" : name,
            "phones" : phones,
            "working_hours" : working_hours
        }
    )

# # print(table_head)

with open('all_city_dict.json', 'w', encoding='utf-8') as file:
    json.dump(all_city_dict, file, indent=4, ensure_ascii=False)