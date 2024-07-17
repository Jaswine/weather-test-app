from unittest import TestCase
from unittest.mock import patch, MagicMock

from base.api.services import get_data_from_api, get_all_cities
from base.models import City


class ServicesAPITest(TestCase):
    def setUp(self):
        self.test_data = {
            'weather': [{'main': 'Rain'}],
            'main': {'temp': 26.89},
            'name': 'Pavlodar'
        }
        self.city = City.objects.create(name="City1", count=100000)

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

    def test_get_all_cities_success(self):
        data = get_all_cities()

        self.assertIsNotNone(data)
        self.assertIn(data, self.city)

    def tearDown(self):
        self.city.delete()


