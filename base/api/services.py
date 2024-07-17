
from django.conf import settings
import requests


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
