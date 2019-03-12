import requests
import json

API_ROOT = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?'


class NoKeyException(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return repr(self.error)


class NoResponseException(Exception):
    def __init__(self, query, response):
        self.response = response

    def __str__(self):
        return repr('GET %s %s' % (self.query, self.response))


class NYTSearch(object):
    def __init__(self, key=None):
        self.key = key
        if key is None:
            raise NoKeyException('No Key provided')

    def search(self, terms):
        terms_formatted = 'q=' + terms.replace(' ', '+')
        api_key = '&api-key='+self.key
        query = API_ROOT + terms_formatted + api_key
        response = requests.get(query)
        if response.status_code != 200:
            raise NoResponseException(query, response.status_code)
        else:
            return response.json()
