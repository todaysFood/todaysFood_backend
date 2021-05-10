import requests
import json
import heapq
from pprint import pprint


class kakao_local:

    def __init__(self):

        url = 'https://dapi.kakao.com/v2/local/'
        self.rest_api_key = '7b8fcbc7d75b30e51cee4e9ee3634957'
        self.headers = {"Authorization" : "KakaoAK {}".format(self.rest_api_key)}

        self.URL_address = url + 'search/address.json'
        self.URL_region = url + 'geo/coord2regioncode.json'
        self.URL_coord2address = url + 'geo/coord2address.json'
        self.URL_transcoord = url + 'geo/transcoord.json'
        self.URL_keyword = url + 'search/keyword.json'
        self.URL_category = url + 'search/category.json'

    def search_address(self, query, analyze_type=None, page=None, size=None):

        params = {"query" : f"{query}"}

        if analyze_type != None:
            params["analyze_type"] = f"{analyze_type}"

        if page != None:
            params['page'] = f"{page}"

        if size != None:
            params['size'] = f"{size}"

        res = requests.get(self.URL_address, headers=self.headers, params=params)

        document = json.loads(res.text)

        return document

    def search_keyword(self, query, category_group_code=None, x=None, y=None, radius=None, rect=None, page=None, size=None, sort=None):

        params = {"query" : f"{query}"}

        if x != None:
            params['x'] = x

        if y:
            params['y'] = y

        if sort != None:
            params['sort'] = sort

        if page:
            params['page'] = page

        if radius:
            params['radius'] = radius

        if category_group_code:
            params['category_group_code'] = category_group_code

        if size:
            params['size'] = size


        res = requests.get(self.URL_keyword, headers=self.headers, params=params)

        document = json.loads(res.text)
        return document

