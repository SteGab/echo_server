import requests
import json
import logging

logging.basicConfig(level=logging.INFO)

def test_send():
    nestedObj = {
        "value1": "No1",
        "value2": "No2"
    }
    
    nestedString = json.dumps(nestedObj)
    
    payload_obj = {
        "Param1": "Parameter1",
        "nested": nestedString
    }
    payload_str = json.dumps(payload_obj)
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    response = requests.post(url="http://localhost:8000/echo-post", json=payload_str, headers=headers)
    
    
    assert response.status_code == 200
    
    response_raw = response.text
    logging.info(f"Response Raw: {response_raw}")
    response_json = response.json()
    #logging.info(f"Response JSON: {response_json}")
    logging.info(f"Response JSON: {response_json['received_data']}")
