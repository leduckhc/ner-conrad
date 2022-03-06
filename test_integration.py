import requests

def test_ner():
    response = requests.post("http://127.0.0.1:8000/ner", json={"text": "Rapoo 2.4Ghz Bluetooth Wireless Headset with Microphone (H6020 Black)"})
    assert response.status_code == 200
    r_obj = response.json()
    assert r_obj.get("entities")
    assert r_obj["entities"] == [{'text': 'Rapoo', 'label': 'BRAND', 'start_char': 0, 'end_char': 5}]
