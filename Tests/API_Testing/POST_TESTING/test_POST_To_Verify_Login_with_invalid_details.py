import json
import pytest
from jsonschema import validate
from API_CLIENTS.POST_API.post_To_Verify_Login_with_valid_details import post_To_Verify_Login_with_valid_details_class
from Payloads.commom_payload import payloads

@pytest.mark.smoke
def test_POST_To_Verify_Login_with_valid_details():
    email = "rohitjuyal114441@gmail.com"
    password = "Rohitjuyal"

    response = post_To_Verify_Login_with_valid_details_class.test_post_To_Verify_Login_with_valid_details(email=email,password=password,payload=None)
    print("Status code ",response.status_code)
    print("Response Text", response.text)
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()
    with open("Schemas/post_To_Verify_Login_with_valid_details_schemas.json") as f:
        schema = json.load(f)

    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")
