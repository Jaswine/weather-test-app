from django.conf import settings
import requests

from base.models import City


def get_data_from_api(city: str) -> dict | None:
    """
       Взятие данных с апи
        :param city: str - Город
        :return: dict - Данные
    """
    response = requests.get(settings.OPEN_WEATHER_MAP_API, {
        'q': city,
        'appid': settings.OPEN_WEATHER_MAP_API_KEY,
        'units': 'metric',
    })

    if response.status_code == 200:
        return response.json()
    return None


def create_or_update_city(city: str) -> City | None:
    """
        Создание или обновление информации о городе

        :param city:
        :return: City | None
    """
    existing_city = City.objects.filter(name=city).first()
    if existing_city:
        existing_city.count = existing_city.count + 1
        existing_city.save()
        return existing_city
    return City.objects.create(name=city, count=1)
