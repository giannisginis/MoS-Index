from app.main.service.handler import Handler
from app.main.utils.config import BaconIpsumMeta


class MockResponse:
    def __init__(self, status_code: int, text: str):
        self.status_code = status_code
        self.text = text


def test_handler_bitly(mocker):
    mocker.patch('app.main.service.handler.requests.get',
                 return_value=MockResponse(status_code=200, text="Hi i am a mock Response"))

    response = Handler(api_provider=BaconIpsumMeta.API_URL, params={"type": "all-meat", "sentences": 3}).get_request()

    assert response.text == "Hi i am a mock Response"
    assert response.status_code == 200