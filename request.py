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


def get_weather(city):
    """Получение информации о погоде"""
    coordinates = get_city_coord(city).split()
    payload = {"lat": coordinates[1], "lon": coordinates[0], "lang": "ru_RU"}
    r = requests.get(
        "https://api.weather.yandex.ru/v2/forecast",
        params=payload,
        headers=config.weather_key,
    )
    weather_data = json.loads(r.text)
    return weather_data