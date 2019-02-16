"""
Author Emmanuel Paul

"""
import json
from pprint import pprint
import urllib
import requests
from .my_logger import get_logger
from .request_config import REMOTE_HOST, REMOTE_PORT

logger = get_logger()

class DjangoClient:
    def __init__(self):
        self.error_case = []

    def get(self, url):
        url = "http://%s:%d"%(REMOTE_HOST,REMOTE_PORT) + url
        logger.info("url:{}".format(url))

        res = requests.get(url)
        
        if res.status_code != 200:
            return json.dumps(res.text)
        
        try:
            dct = json.loads(res.text) # Dictionary of Data Loaded from resource
            return json.dumps(dct)
        except ValueError:
            logger.info("Error: Could not read response")
            return "Error reading from response"

        
    def post(self, url, data):
        post_url = "http://%s:%d"%(REMOTE_HOST,REMOTE_PORT) + url
        res =  self.get(url)
        dct = json.loads(res)
        csrfmiddlewaretoken = dct.get('csrfmiddlewaretoken')
        data.update({"csrfmiddlewaretoken":csrfmiddlewaretoken})
        try:
            res = urllib.request.urlopen(post_url, urllib.parse.urlencode(data))
        except urllib.error.HTTPError:
            self.error_case.append(url)
            return "500"
        if res.code != 200:
            self.error_case.append(url)
            return res.read()
        try:
            dct = json.loads(res.read())
        except ValueError:
            return res.read()

        return json.dumps(dct, indent=1)
