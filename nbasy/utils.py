from requests import get
from datetime import datetime


# Constants
TODAY = datetime.today()
BASE_URL = 'http://stats.nba.com/stats/{endpoint}/'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),  # noqa: E501
    'Dnt': ('1'),
    'Accept-Encoding': ('gzip, deflate, sdch'),
    'Accept-Language': ('en'),
    'origin': ('http://stats.nba.com')
}


def _get_json(endpoint, params, referer='scores'):
    """
    Internal method to streamline our requests / json getting

    Args:
        endpoint (str): endpoint to be called from the API
        params (dict): parameters to be passed to the API

    Raises:
        HTTPError: if requests hits a status code != 200

    Returns:
        json (json): json object for selected API call

    """

    h = dict(HEADERS)
    h['referer'] = 'http://stats.nba.com/{ref}/'.format(ref=referer)
    _get = get(
        BASE_URL.format(endpoint=endpoint),
        params=params,
        headers=h
    )

    # print _get.url
    _get.raise_for_status()

    return _get.json()