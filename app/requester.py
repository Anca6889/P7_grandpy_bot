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
        """ Send a request to Wikipedia API with the user text """

        url = "https://fr.wikipedia.org/w/api.php"
        payload = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": "{}".format(self.query),
            "srlimit": "1"
        }
        if self.query == []:  # if no query reach Grandpy
            self.wiki_result = random.choice(c.GRANDPY_EMPTY)
            
        else:
            try:
                request = requests.get(url, params=payload)
                json = request.json()
                self.get_wiki_page_id(json)
                
            except ValueError: # if no wikipedia result
                self.wiki_result = random.choice(c.GRANDPY_DONT_UNDERSTAND)
                

    def get_wiki_page_id(self, json):
        """ get the page_id of the first request """

        try:
            data = json
            pages = data['query']['search']
            for key, value in enumerate(pages):
                page_id = str(value['pageid'])
            self.second_request_wiki(page_id)
            
        except UnboundLocalError:
            self.wiki_result = random.choice(c.GRANDPY_DONT_UNDERSTAND)


    def second_request_wiki(self, page_id):
        """ Send a second request with the page_id to extract datas """

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
        self.get_wiki_coordinates(json)

    def get_wiki_text(self, json):
        """ get the text of extracted datas """

        data = json
        print(data)
        pages = data['query']['pages']
        for k, v in pages.items():
            self.wiki_result = [random.choice(c.GRANDPY_KNOWS) + str(
                v['extract']) + random.choice(c.GRANDPY_END)]
        print(self.wiki_result)

    def get_wiki_coordinates(self, json):
        """ get the coordinates of the wikipedia page if it is a place """
        try:
            data = json
            pages = data['query']['pages']
            for k, v in pages.items():
                coordinates = (
                    v['coordinates'][0]['lat'], v['coordinates'][0]['lon'])
            lat = str(coordinates[0])
            lng = str(coordinates[1])
            strco = lat +" "+ lng
            print(strco)
            self.request_maps(strco)
        except KeyError:
            pass

    def request_maps(self, strco):
        """
        Send a request to Google Maps API with the coordinates get from 
        wikipedia
        """
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        payload = {"key": "",
                "location": strco,
                "radius": "1500"
                }
        request = requests.get(url, params=payload)
        json = request.json()
        print(json)
        return json


if __name__ == '__main__':
    request = Request(["tour", "europe", "mulhouse"])
    # request.request_maps()
