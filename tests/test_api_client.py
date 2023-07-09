import unittest
from unittest.mock import patch, MagicMock
from requests.exceptions import RequestException
from src.api.api_client import get_timezones_api

class APIClientTestCase(unittest.TestCase):
    @patch('src.api.api_client.requests.get')
    def test_get_timezones_api_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "status": "OK",
            "message": "",
            "zones": [
                {
                    "countryCode": "US",
                    "countryName": "United States",
                    "zoneName": "America/New_York",
                    "gmtOffset": -14400,
                    "timestamp":1688899696
                },
                {
                    "countryCode": "GB",
                    "countryName": "United Kingdom",
                    "zoneName": "Europe/London",
                    "gmtOffset": 3600,
                    "timestamp": 1688917696
                }
            ]
        }
        mock_get.return_value = mock_response

        expected_timezones = [
            {
                "countrycode": "US",
                "countryname": "United States",
                "zonename": "America/New_York",
                "gmtoffset": -14400
            },
            {
                "countrycode": "GB",
                "countryname": "United Kingdom",
                "zonename": "Europe/London",
                "gmtoffset": 3600
            }
        ]

        timezones = get_timezones_api()

        self.assertEqual(timezones, expected_timezones)

    @patch('src.api.api_client.requests.get')
    def test_get_timezones_api_no_zones(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "message": "No zones available"
        }
        mock_get.return_value = mock_response

        timezones = get_timezones_api()

        self.assertIsNone(timezones)

    @patch('src.api.api_client.requests.get')
    def test_get_timezones_api_request_error(self, mock_get):
        mock_get.side_effect = RequestException("Network error")

        timezones = get_timezones_api()

        self.assertIsNone(timezones)

    @patch('src.api.api_client.requests.get')
    def test_get_timezones_api_value_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.side_effect = ValueError("Invalid JSON response")
        mock_get.return_value = mock_response

        timezones = get_timezones_api()

        self.assertIsNone(timezones)

if __name__ == '__main__':
    unittest.main()