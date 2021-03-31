from app.tests.test_main import client


def test_random():
    url = "random/?type=all-meat&sentences=3"
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.json()['text'].split(".")) == 4


def test_attribute():
    url = "attribute/?attribute_name=egressQosClassification"
    response = client.get(url)
    assert response.json()['datatype'] == "moRef"


def test_class():
    url = "class/?class_name=Transport/VlanPort"
    response = client.get(url)
    for l in response.json():
        if l["attribute"] == ["egressQosClassification"]:
            assert l["attribute"]["egressQosClassification"] == "moRef"
            assert l["attribute"]["egressQosClassification"] == "moRef"


def test_datatype():
    url = "datatype/?datatype=int32"
    response = client.get(url)
    assert "x2retryTimerMaxAuto" in response.json()['attributes']
