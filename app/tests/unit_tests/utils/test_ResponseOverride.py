from app.main.utils.ResponseOverride import ResponseOverride


def test_ResponseOverride():
    instance = ResponseOverride(status_code=400, sequence='Hi i am a test sequence', message="OK")
    assert instance.get_status_code() == 400
    assert instance.get_sequence() == 'Hi i am a test sequence'
    assert instance.get_message() == "OK"

    assert instance.to_dict() == {"status_code": 400, "text": 'Hi i am a test sequence', "message": "OK"}