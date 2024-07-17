from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.response import Response

from base.api.serializers import CitySerializer
from base.api.services import get_weather_data, get_all_cities


class WeatherAPIView(APIView):
    def get(self, request, city):
        """
            Вывод погоды для конкретного города
        """
        content, status_code = get_weather_data(city)
        return Response(content, status=status_code)


class CityListAPIView(APIView):
    def get(self, request):
        """
            Вывод статистики показа городов
        """
        cities = get_all_cities()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
