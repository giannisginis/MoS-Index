from app.main.utils.ResponseOverride import ResponseOverride
from app.main.utils.config import *
from app.main.service.handler import Handler


class BaconIpsum:
    def __init__(self, type: str, sentences: int = 3):
        self.type = type
        self.sentences = sentences
        self.params = {"type": type, "sentences": sentences}
        self.handler = Handler(api_provider=BaconIpsumMeta.API_URL, params=self.params)

    def _make_request(self):
        response = self.handler.get_request()
        return ResponseOverride(status_code=response.status_code, sequence=response.text)

    @staticmethod
    def _clean_string(string):
        a = '[]"'
        for char in a:
            string = string.replace(char, "")
        return string.strip()

    def run(self):
        results = self._make_request()
        if results.get_status_code() not in [200, 201]:
            pass
        else:
            return {"status_code": results.get_status_code(),
                    "text": self._clean_string(results.get_sequence())}
