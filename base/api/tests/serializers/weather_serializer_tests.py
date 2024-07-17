from unittest import TestCase

from base.api.serializers import WeatherSerializer


class WeatherSerializerTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'weather_main': 'Rain',
            'weather_description': 'light rain',
            'weather_icon': '10d',
            'temp': 26.89,
            'city_name': 'Pavlodar'
        }

    def test_serializer_with_valid_data(self):
        weather_instance = WeatherSerializer(data=self.valid_data)

        self.assertIsNotNone(weather_instance)
        self.assertTrue(weather_instance.is_valid())

    def test_serializer_with_invalid_data(self):
        self.valid_data.pop('city_name')

        serializer = WeatherSerializer(data=self.valid_data)

        self.assertFalse(serializer.is_valid())


