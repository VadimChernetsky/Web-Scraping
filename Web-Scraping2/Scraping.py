import requests
from bs4 import BeautifulSoup
import json
import os
import time


def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) "
                      "Version/11.0 Mobile/15A5341f Safari/604.1"
    }

    games_data_list = []
    iteration_count = 4412
    print(f"Всего итераций: #{iteration_count}")

    for item in range(1, 4413):
        req = requests.get(url + f"?page={item}", headers)
        # print(req.text)

        # К папкам добовляем номер итерации
        folder_name = f"data/data_{item}"

        # Проверка, если папка уже существует, то движемся дальше
        if os.path.exists(folder_name):
            print("Папка уже существует")
        else:
            os.mkdir(folder_name)

        # Записал в файл
        with open(f"{folder_name}/games_{item}.html", "w", encoding='utf-8') as file:
            file.write(req.text)

        # # Прочитал файл и записал в переменную
        with open(f"{folder_name}/games_{item}.html", encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        games = soup.find_all("div", class_="BaseElementCard_card__ZIifM")
        # print(games)

        games_url = []
        for game in games:
            game_url = "https://kanobu.ru" + game.find("a").get("href")
            games_url.append(game_url)
            # print(game_url)

        # Получаем название игр
        for game_url in games_url:
            req = requests.get(game_url, headers)
            game_name = game_url.split("/")[-2]
            # print(game_name)

            # Сохраняем файл
            with open(f"{folder_name}/{game_name}.html", "w", encoding='utf-8') as file:
                file.write(req.text)

            # Считываем в переменную
            with open(f"{folder_name}/{game_name}.html", encoding='utf-8') as file:
                src = file.read()

            # Извлекаем данные
            soup = BeautifulSoup(src, "lxml")
            game_data = soup.find("div", class_="baseElementLayout_body__qOxgC")
            # print(game_data)

            # Получаем картинку
            try:
                game_logo = game_data.find("aside", class_="DatabaseElementCover_cover__3dISW").find("img").get("src")
                # print(game_logo)
            except Exception:
                game_logo = "No game logo"

            # Получаем описание игры
            try:
                game_description = game_data.find("div", class_="DatabaseElementContent_content_head__ObqOK").find("p").text
                # print(game_description)
            except Exception:
                game_description = "No game description"

            # Получаем дату выхода
            try:
                game_the_date = game_data.find("span", class_="DatabaseElementOption_option_value__U0zWT").text
                # print(game_the_date)
            except Exception:
                game_the_date = "No game the date"

            # Получаем платформу
            try:
                game_platform = game_data.find_all("span", class_="DatabaseElementOption_option_value__U0zWT")[1].text
                # print(game_platform)
            except Exception:
                game_the_date = "No game platform"

            # Получаем жанр
            try:
                game_genre = game_data.find_all("span", class_="DatabaseElementOption_option_value__U0zWT")[2].text
                # print(game_genre)
            except Exception:
                game_genre = "No game genre"

            games_data_list.append(
                {
                    "Название игры": game_name,
                    "URL Логотип игры": game_logo,
                    "Описание игры": game_description,
                    "Платформа": game_platform,
                    "Жанр": game_genre,
                    "Cайт игры": game_url
                }
            )

        # print(games_data_list)

        iteration_count -= 1
        print(f"Итерация #{item} завершина, осталось итераций #{iteration_count}")
        if iteration_count == 0:
            print("Сбор данных завершен")
        time.sleep(2)

    # Сохранение словаря в json
    with open("data/games_data.json", "a", encoding="utf-8") as file:
        json.dump(games_data_list, file, indent=4, ensure_ascii=False)

get_data("https://kanobu.ru/games/new/")

