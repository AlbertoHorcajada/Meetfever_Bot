import requests
import json

from model.Data import Data
from collections import namedtuple

def custom_data_decoder(response_data_dictionary):
    return namedtuple("X", response_data_dictionary.keys())(*response_data_dictionary.values())


class WebService:
    
    def __init__(self, url: str):
        self.url = url
    
    def get_request_json(self):
        resp = requests.get(self.url, timeout=5)
        print(resp.text)
        json_string = resp.text
        x: Data = json.loads(json_string, object_hook=custom_data_decoder)
        if x.data.RETCODE == 0:
            return x.data.JSON_OUT
        else:
            return None