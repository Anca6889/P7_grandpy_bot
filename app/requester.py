""" This module is request the Google Maps & Wikipedia API's with the
parsed message """

import requests, random
from app.config import config as c


class Request:
    """ this class will send the request to the API's """

    def __init__(self, query):

        self.query = query
        self.wiki_result = None
        self.first_request_wiki()

    def first_request_wiki(self):
        """
        Send a request to Wikipedia API with the user text
        """

        url = "https://fr.wikipedia.org/w/api.php"
        payload = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": "{}".format(self.query),
            "srlimit": "1"
        }
        if self.query == []:
            self.wiki_result = random.choice(c.GRANDPY_EMPTY)
            
        else:
            try:
                request = requests.get(url, params=payload)
                json = request.json()
                self.get_wiki_page_id(json)
                
            except ValueError:
                self.wiki_result = random.choice(c.GRANDPY_DONT_UNDERSTAND)

    def get_wiki_page_id(self, json):

        try:
            data = json
            pages = data['query']['search']
            for key, value in enumerate(pages):
                page_id = str(value['pageid'])
            self.second_request_wiki(page_id)
            
        except UnboundLocalError:
            self.wiki_result = random.choice(c.GRANDPY_DONT_UNDERSTAND)


    def second_request_wiki(self, page_id):

        url = "https://fr.wikipedia.org/w/api.php"
        payload = {
            "action": "query",
            "format": "json",
            "prop": "extracts|coordinates",
            "exsentences": "5",
            "explaintext": "1",
            "exsectionformat": "plain",
            "pageids": page_id
        }
        request = requests.get(url, params=payload)
        json = request.json()
        self.get_wiki_text(json)
        # self.get_wiki_coordinates(json)

    def get_wiki_text(self, json):

        data = json
        print(data)
        pages = data['query']['pages']
        for k, v in pages.items():
            self.wiki_result = str(v['extract'])
        print(self.wiki_result)

    # def get_wiki_coordinates(self, json):

    #     data = json
    #     pages = data['query']['pages']
    #     for k, v in pages.items():
    #         coordinates = (
    #             v['coordinates'][0]['lat'], v['coordinates'][0]['lon'])
    #     print(coordinates)

    def request_maps(self):
        """
        Send a request to Google Maps API
        """
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        payload = {"key": "",
                   "query": self.query}
        request = requests.get(url, params=payload)
        json = request.json()
        print(json)
        return json


if __name__ == '__main__':
    request = Request(["tour", "europe", "mulhouse"])
    # request.request_maps()
