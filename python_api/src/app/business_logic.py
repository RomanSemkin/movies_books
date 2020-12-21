import json
import requests

from django.conf import settings
from django.utils.http import quote


def send_request_to_imdb(title: str, plot: str = None, year: str = None) -> json:
    url = f"{settings.IMDB_URL}?apikey={settings.IMDB_API_KEY}"
    if plot:
        url = f"{url}&plot={quote(plot)}"
    elif year:
        url = f"{url}&y={quote(year)}"
    url = f"{url}&t={quote(title)}"
    res = requests.get(url=url)
    return json.loads(res.content.decode())


def send_request_to_open_lib(book_id: str) -> json:
    url = f"{settings.OPEN_LIBRARY_URL}isbn/{book_id}.json"
    res = requests.get(url=url)
    return json.loads(res.content.decode())
