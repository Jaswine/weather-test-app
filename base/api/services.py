from typing import Tuple

from django.conf import settings
import requests
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from base.api.serializers import WeatherSerializer
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


def get_weather_data(city: str) -> Tuple[dict, int]:
    """
        Взятие данных о погоде

        :param city:str - Город
        :return: Tuple[dict, int]
    """
    data = get_data_from_api(city)

    if data is not None:
        serializer = WeatherSerializer(data={
            'weather_main': data.get('weather', [{}])[0].get('main'),
            'weather_description': data.get('weather', [{}])[0].get('description'),
            'weather_icon': data.get('weather', [{}])[0].get('icon'),
            'temp': data.get('main', {}).get('temp'),
            'city_name': data.get('name')
        })

        if serializer.is_valid():
            return serializer.data, HTTP_200_OK
        return serializer.errors, HTTP_400_BAD_REQUEST

    return {'message': 'City not found'}, HTTP_404_NOT_FOUND


def get_all_cities() -> list[City]:
    """
        Вывод списка городов

        :return: list[City]
    """
    return City.objects.all()
