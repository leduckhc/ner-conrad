import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_ner():
    response = client.post("/ner", json={"text": "Rapoo 2.4Ghz Bluetooth Wireless Headset with Microphone (H6020 Black)"})
    assert response.status_code == 200
    r_obj = response.json()
    assert r_obj.get("entities")
    assert r_obj["entities"] == [{'text': 'Rapoo', 'label': 'BRAND', 'start_char': 0, 'end_char': 5}]
