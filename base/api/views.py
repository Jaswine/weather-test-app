from rest_framework.status import (HTTP_404_NOT_FOUND,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.response import Response

from base.api.serializers import WeatherSerializer
from base.api.services import get_data_from_api


class WeatherAPIView(APIView):
    def get(self, request, city):
        """
            Вывод погоды для конкретного города
        """
        data = get_data_from_api(city)

        if data is not None:
            serializer = WeatherSerializer(data={
                'weather_main': data.get('weather', {})[0].get('main'),
                'weather_description': data.get('weather', {})[0].get('description'),
                'weather_icon': data.get('weather', {})[0].get('icon'),
                'temp': data.get('main', {}).get('temp'),
                'city_name': data.get('name')
            })
            if serializer.is_valid():
                return Response(serializer.data,
                                status=HTTP_200_OK)
            return Response(serializer.errors,
                            status=HTTP_400_BAD_REQUEST)
        return Response({
            'message': 'City not found'
        }, status=HTTP_404_NOT_FOUND)
