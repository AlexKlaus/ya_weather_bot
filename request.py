import json

import requests

import config


def get_city_coord(city):
    """Получение координат города"""
    # Задаем параметры запроса для получения координат_
    payload = {"geocode": city, "apikey": config.geo_key, "format": "json"}
    # Отправляем GET-запрос к API Yandex Maps Geocoding
    r = requests.get("https://geocode-maps.yandex.ru/1.x", params=payload)
    # Преобразуем ответ в JSON-формат
    geo = json.loads(r.text)
    # Извлекаем координаты из полученного JSON
    return geo["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"][
        "Point"
    ]["pos"]
