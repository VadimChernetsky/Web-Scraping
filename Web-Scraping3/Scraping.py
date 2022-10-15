import requests
from bs4 import BeautifulSoup
import json

phones_dict_2 = {}
count = 0

while True:

    url = f"https://www.a1.by/ru/shop/c/phones?q=%3Arelevance&page={count}"

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 "
                      "(KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
    }

    req = requests.get(url, headers=headers)
    src = req.text
    # print(src)

    # with open("index.html", "w", encoding='utf-8') as file:
    #     file.write(src)

    # with open("index.html", encoding='utf-8') as file:
    #     src = file.read()

    # soup = BeautifulSoup(src, "lxml")
    # phones_name = soup.find_all(class_="product-search-item-title")[0]
    # phones_RAM = soup.find_all(class_="product-memory--current")[0]
    # phones_price = soup.find_all("span", class_="price-value")[1]
    #
    # phones_dict = {}
    # for name in phones_name:
    #     phones_dict['name'] = name.text
    # for ram in phones_RAM:
    #     phones_dict['RAM'] = ram.text
    # for price in phones_price:
    #     phones_dict['price'] = f'{price}' + 'rub'
    # print(phones_dict)

    soup = BeautifulSoup(src, "lxml")
    # phones_name = soup.find(class_="product-listing-item-title").text
    # phones_price = soup.find(class_="one-time-charge").text
    phones_name = soup.find_all(class_="product-listing-item-title")
    phones_price = soup.find_all(class_="one-time-charge")

    phones_name_text = []
    phones_price_text = []

    for name in phones_name:
        phones_name_text.append(name.text)
    for price in phones_price:
        x = price.text
        y = " ".join(x.split())
        phones_price_text.append(y)



    phones_dict = dict(zip(phones_name_text, phones_price_text))
    print(phones_dict)
    for key, value in phones_dict.items():
        phones_dict_2[key] = value

    count += 1

    if phones_dict == {}:
        break

with open("phones_dict.json", 'w', encoding='utf-8') as file:
    json.dump(phones_dict_2, file, indent=4, ensure_ascii=False)


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



