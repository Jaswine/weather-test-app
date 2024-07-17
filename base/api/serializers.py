from rest_framework.serializers import Serializer, CharField, FloatField, ModelSerializer

from base.models import City


class WeatherSerializer(Serializer):
    weather_main = CharField()
    weather_description = CharField()
    weather_icon = CharField()
    temp = FloatField()
    city_name = CharField()


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'count', )
