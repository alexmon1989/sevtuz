from django.conf import settings
import urllib.parse
import urllib.request
from urllib.error import URLError
import json


def get_radario_events():
    """Возвращает список текущих событий из Radario."""
    url = '{}/events?limit=100'.format(settings.RADARIO_API_BASE_PATH)
    headers = {
        'api-id': settings.RADARIO_API_ID,
        'api-key': settings.RADARIO_API_KEY,
        'api-version': settings.RADARIO_API_VERSION
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.load(response)
    except URLError:
        return {}
    except json.JSONDecodeError:
        return {}
    return data
