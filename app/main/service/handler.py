from typing import Dict, Any
from urllib.parse import urlencode
import requests
from app.main.utils.ResponseOverride import ResponseOverride
from app.main.utils.config import *


class Handler:
    def __init__(self, api_provider: str = None, params: Dict[str, Any] = None,
                 headers: Dict[str, Any] = None):
        self.api_provider = api_provider
        self.parameters = params
        self.headers = headers

    def get_request(self):
        try:
            url = self.api_provider + "?" + urlencode(
                {BaconIpsumMeta.TYPE: self.parameters["type"]}) + "&" + urlencode(
                {BaconIpsumMeta.SENTENSES: self.parameters["sentences"]})
            return requests.get(url)
        except requests.exceptions.Timeout:
            return ResponseOverride(status_code=408)
