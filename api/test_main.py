import unittest
from unittest.mock import patch, MagicMock
from main import app

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_root_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    @patch('api.main.get_data')
    def test_data_endpoint(self, mock_get_data):
        mock_data = {'key': 'value'}
        mock_get_data.return_value = mock_data
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_data)

    def test_data_endpoint_error(self):
        with patch('api.main.get_data', side_effect=Exception('Error')):
            response = self.app.get('/data')
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.data, b'Error retrieving data')

    def test_post_endpoint(self):
        data = {'key': 'value'}
        response = self.app.post('/post', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Data received successfully')

    def test_post_endpoint_invalid_data(self):
        response = self.app.post('/post', data='invalid')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'Invalid data format')
