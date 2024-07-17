from unittest import TestCase
from unittest.mock import patch, MagicMock

from base.api.services import get_data_from_api
from base.models import City
from base.services import create_or_update_city


class ServicesTest(TestCase):
    def setUp(self):
        self.test_data = {
            'weather': [{'main': 'Rain'}],
            'main': {'temp': 26.89},
            'name': 'Pavlodar'
        }
        self.city = City.objects.create(name='UniqueCity', count=1)

    @patch('requests.get')
    def test_get_data_from_api_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.test_data

        mock_get.return_value = mock_response

        data = get_data_from_api('Pavlodar')

        self.assertIsNotNone(data)
        self.assertEqual(data, self.test_data)

    @patch('requests.get')
    def test_get_data_from_api_failure(self, mock_get):
        mock_response = {'status_code': 404}
        mock_get.return_value = type('MockResponse', (), mock_response)

        data = get_data_from_api('abcd')

        self.assertIsNone(data)

    def test_create_or_update_city_when_city_is_exists(self):
        data = create_or_update_city(self.city.name)

        self.assertIsNotNone(data)
        self.assertEqual(data, self.city)
        self.assertEqual(data.count, self.city.count + 1)

    def test_create_or_update_city_when_city_is_not_exists(self):
        data = create_or_update_city('UniqueCity1')

        self.assertIsNotNone(data)

        self.assertEqual(data.name, 'UniqueCity1')
        self.assertEqual(data.count, 1)

    def tearDown(self):
        self.city.delete()
        city1 = City.objects.filter(name='UniqueCity1').first()
        city1.delete() if city1 else None
