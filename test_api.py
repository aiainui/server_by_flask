import requests
import json

BASE_URL = "http://xxx:13020"

def test_index():
    print("Testing index interface: GET /")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        if response.status_code == 200 and response.text == "ok!!":
            print("Index test passed!\n")
        else:
            print("Index test failed!\n")
    except Exception as e:
        print(f"Error testing index: {e}\n")

def test_call_back():
    print("Testing call_back interface: POST /call_back")
    payload = {
        "code": 20000,
        "requestId": "test_request_123",
        "data": {
            "emotion": {
                "total": {
                    "score": 0.85
                }
            }
        }
    }
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(
            f"{BASE_URL}/call_back", 
            data=json.dumps(payload), 
            headers=headers
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        if response.status_code == 200 and response.json().get('code') == 20000:
            print("Call_back test passed!\n")
        else:
            print("Call_back test failed!\n")
    except Exception as e:
        print(f"Error testing call_back: {e}\n")

if __name__ == "__main__":
    print(f"Starting API tests on {BASE_URL}...\n")
    test_index()
    test_call_back()

