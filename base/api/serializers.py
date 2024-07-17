from rest_framework.serializers import Serializer, CharField, FloatField


class WeatherSerializer(Serializer):
    weather_main = CharField()
    weather_description = CharField()
    weather_icon = CharField()
    temp = FloatField()
    city_name = CharField()
