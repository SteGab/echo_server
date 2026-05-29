import requests
import json
import logging

logging.basicConfig(level=logging.INFO)

def test_send():
    nestedObj = {
        "value1": "No1",
        "value2": "No2"
    }
    
    #nestedString = json.dumps(nestedObj).replace("'", "\"")
    nestedString = json.dumps(nestedObj)
    
    payload = {
        "Param1": "Parameter1",
        "nested": nestedString
    }
    response = requests.post(url="http://localhost:8000/echo-post", json=json.dumps(payload))
    assert response.status_code == 200
    response_json = response.json()
    #logging.info(f"Response JSON: {response_json}")
    logging.info(f"Response JSON: {response_json['received_data']}")
