"""Functions that used to scrape the message data from the url"""

import json

import requests

from .utils import add_to_json


def get_url(symbol, next_id=None):
    """Return the url to scrape with query symbol

    Args:
        symbol (string): the symbol to search for (e.g. ETH.X)
    Returns:
        string: the url to scrape
    """
    if next_id is None:
        url = "https://api.stocktwits.com/api/2/streams/symbol/{}.json?filter=all&limit=20".format(
                symbol)
    else:
        url = "https://api.stocktwits.com/api/2/streams/symbol/{}.json?filter=all&limit=20&max={}".format(
                symbol, next_id)
    return url


def get_response(url, headers=None, payload=None):
    """Return the response from the url

    Args:
        url (string): the url to scrape
        headers (dict): the headers to send with the request
        payload (dict): the payload to send with the request
    Returns:
        response: the response from the url as json
    """
    if headers is None:
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
        }
    if payload is None:
        payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def init_scrape(outfile, query, num_twits):
    """Initialize the scrape and return the next_id and twits_left,
    output the first 20 scraped entries to the file
    Args:
        outfile (json): the file to save the data to
        query (string): the query to search for (e.g. ETH.X)
        num_twits (int): the number of twits to scrape
    Returns:
        next_id: the next_id to scrape from
        twits_left: the number of twits left to scrape
    """
    url = get_url(query)
    response = get_response(url)
    outfile = open(outfile, "w")
    outfile.write(json.dumps(response['messages'], indent=4))
    print(
            f"{len(response['messages'])}/{num_twits} messages added to the file")
    twits_left = num_twits - len(response['messages'])
    return response['cursor']['max'], twits_left


def scrape(outfile, query, num_twits):
    """Scrape the data from the url and save to a file

    Args:
        outfile (string): the file to save the data to
        query (string): the query to search for (e.g. ETH.X)
        num_twits (int): the number of twits to scrape
    """
    next_id, twits_left = init_scrape(outfile, query, num_twits)
    twits_scraped = 20
    while twits_left > 0:
        url = get_url(query, str(next_id))
        response = get_response(url)
        add_to_json(outfile, response['messages'])
        next_id = response['cursor']['max']
        twits_left = twits_left - len(response['messages'])
        twits_scraped += len(response['messages'])
        print(f"{twits_scraped}/{num_twits} messages added to the file")
