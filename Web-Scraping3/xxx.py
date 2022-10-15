from bs4 import BeautifulSoup
import re
import requests
import lxml
#открывем файл нашей страницы(на чтение)
with open("index2.html", encoding='utf-8') as file:
    src = file.read()
print(src)

#устанавливаем швейцарски нож 'pip install beautifulsoup4'

soup = BeautifulSoup(src, "lxml")


#lxml в библиотеке нет, нужно скачивать pip install lxml
# парсим титл(заголовки)
title = soup.title
print(title)
print(title.text)
print(title.string)

# .find() .find_all()
# метод .find() выдаст первый искомый элемент
# метод .find_all() выдаст все искомые элементы и сохр. их в список
page_h1 = soup.find("h1")
print(page_h1)

page_all_h1 = soup.find_all("h1")
print(page_all_h1)
#цикл для того что бы каждый новый эл. выводить с новой строки
for item in page_all_h1:
     print(item.text)

#получаем имя пользователя
#class ключевое зарезервированное слово, поэтому с подчеркиванием
#1 вариант правильный, т.к. это объект "soup" можно применять методы
user_name = soup.find("div", class_="user__name")
print(user_name)
# к объекту применили метод текст
user_name = soup.find("div", class_="user__name")
print(user_name.text)

user_name = soup.find("div", class_="user__name")
print(user_name.text.strip())