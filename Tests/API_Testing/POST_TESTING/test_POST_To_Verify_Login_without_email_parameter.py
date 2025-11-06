import json
import pytest
from jsonschema import validate
from API_CLIENTS.POST_API.POST_To_Verify_Login_without_email_parameter import POST_To_Verify_Login_without_email_parameter_class

@pytest.mark.smoke
def test_POST_To_Verify_Login_without_email_parameter():
    password = "Rohitjuyal"
    response = POST_To_Verify_Login_without_email_parameter_class.POST_To_Verify_Login_without_email_parameter(password=password,payload=None)
    print("Status Code :",response.status_code)
    print("Response Text",response.text)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_json = response.json()
    assert response_json["responseCode"] == 400, f"Expected API responseCode 400, got {response_json['responseCode']}"

    with open("Schemas/POST_To_Verify_Login_without_email_parameter_schemas.json") as f:
        schema = json.load(f)
    if response_json:
        validate(instance=response_json,schema=schema)
    else:
        print(f"Empty list — no transactions found, skipping schema validation.")
