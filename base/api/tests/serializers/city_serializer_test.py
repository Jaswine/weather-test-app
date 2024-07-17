from unittest import TestCase

from base.api.serializers import CitySerializer
from base.models import City


class CitySerializerTest(TestCase):
    def setUp(self):
        self.city = City.objects.create(name='UniqueCity')
        self.valid_data = {
            'name': 'UniqueCity1',
            'count': 1
        }
        self.invalid_data = {
            'name': 'UniqueCity',
            'count': 0
        }

    def test_serializer_with_valid_instance(self):
        serializer = CitySerializer(self.city)
        data = serializer.data

        self.assertIsNotNone(data)
        self.assertEqual(set(data.keys()), {'name', 'count'})
        self.assertEqual(data['name'], self.city.name)
        self.assertEqual(data['count'], self.city.count)

    def test_serializer_with_valid_data(self):
        serializer = CitySerializer(data=self.valid_data)

        self.assertTrue(serializer.is_valid())

    def test_serializer_with_invalid_data(self):
        serializer = CitySerializer(data=self.invalid_data)

        self.assertFalse(serializer.is_valid())

    def tearDown(self):
        self.city.delete()