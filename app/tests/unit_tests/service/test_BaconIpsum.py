from app.main.service.BaconIpsum import BaconIpsum


class MockResponse:
    def __init__(self, status_code: int, text: str):
        self.status_code = status_code
        self.text = text


def test_make_request(mocker):
    mocker.patch('app.main.service.handler.requests.get',
                 return_value=MockResponse(status_code=200, text="Hi i am a mock Response"))

    response = BaconIpsum(type="all-meat")._make_request()

    assert response.sequence == "Hi i am a mock Response"
    assert response.status_code == 200


def test_run_success(mocker):
    mocker.patch('app.main.service.handler.requests.get',
                 return_value=MockResponse(status_code=200, text='[Hi i am a mock Response]"'))

    response = BaconIpsum(type="all-meat").run()

    assert response['text'] == "Hi i am a mock Response"
    assert response['status_code'] == 200


def test_run_fail(mocker):
    mocker.patch('app.main.service.handler.requests.get',
                 return_value=MockResponse(status_code=400, text="Hi i am a mock Response"))

    response = BaconIpsum(type="all-meat").run()

    assert response.message == "Bad Request"
    assert response.status_code == 400
