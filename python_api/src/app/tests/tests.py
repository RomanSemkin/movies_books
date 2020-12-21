import json
from unittest import mock

from django.conf import settings
from django.test import TestCase
from django.utils.http import quote
from rest_framework import status
from rest_framework.response import Response

from app.business_logic import send_request_to_imdb
from .fixtures import imdb_fixture


def get_mock_response(title, year=None, plot=None):
    """
    Function for mocking a method 'get' from requests package.
    """

    def wrapper(url, *args, **kwargs):
        response = Response()
        response.status_code = status.HTTP_200_OK
        IMDB_URl = f"{settings.IMDB_URL}?apikey={settings.IMDB_API_KEY}"
        if f"{IMDB_URl}&t={title}" == url:
            response.content = imdb_fixture
        elif f"{IMDB_URl}&y={year}&t={title}" == url:
            response.content = imdb_fixture
        elif f"{IMDB_URl}&plot={plot}&t={title}" == url:
            response.content = imdb_fixture
        elif f"{IMDB_URl}&plot={plot}&y={year}&t={title}" == url:
            response.content = imdb_fixture
        else:
            raise NotImplementedError
        return response

    return wrapper


class SendRequest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.title = "Matrix"
        cls.year = "1993"
        cls.plot = "short"

    def test_send_request_to_imdb_title(self):
        with mock.patch("requests.get", get_mock_response(self.title)):
            response_data = send_request_to_imdb(self.title)
            self.assertEqual(response_data, json.loads(imdb_fixture.decode()))
            self.assertIn("Title", response_data)
        # url decoding
        undecoded_title = "title with , and ... !! >>> <<< (((__"
        with mock.patch("requests.get", get_mock_response(quote(undecoded_title))):
            response_data = send_request_to_imdb(undecoded_title)
            self.assertEqual(response_data, json.loads(imdb_fixture.decode()))
        with mock.patch(
            "requests.get", get_mock_response(self.title, self.year, self.plot)
        ):
            response_data = send_request_to_imdb(self.title, self.plot, self.year)
            self.assertEqual(response_data, json.loads(imdb_fixture.decode()))
            self.assertIn("Title", response_data)
            self.assertIn("Year", response_data)
            self.assertIn("Plot", response_data)

    def test_send_request_to_imdb_title_with_exception(self):
        # title = None
        with mock.patch("requests.get", get_mock_response(None)):
            with self.assertRaises(TypeError):
                send_request_to_imdb(None)
        # title = []
        with mock.patch("requests.get", get_mock_response([])):
            with self.assertRaises(TypeError):
                send_request_to_imdb([])

    def test_send_request_to_imdb_year(self):
        # year in the url
        with mock.patch(
            "requests.get", get_mock_response(title=self.title, year=self.year)
        ):
            response_data = send_request_to_imdb(title=self.title, year=self.year)
            self.assertEqual(response_data, json.loads(imdb_fixture.decode()))
            self.assertIn("Year", response_data)

    def test_send_request_to_imdb_plot(self):
        # plot in the url
        with mock.patch(
            "requests.get", get_mock_response(title=self.title, plot=self.plot)
        ):
            response_data = send_request_to_imdb(title=self.title, plot=self.plot)
            self.assertEqual(response_data, json.loads(imdb_fixture.decode()))
            self.assertIn("Plot", response_data)
