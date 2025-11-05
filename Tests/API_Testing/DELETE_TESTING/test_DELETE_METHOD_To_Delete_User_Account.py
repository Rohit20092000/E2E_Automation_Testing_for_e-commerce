import json
import pytest
from jsonschema import validate
from API_CLIENTS.DELETE_API.DELETE_METHOD_To_Delete_User_Account import DELETE_METHOD_To_Delete_User_Account_class


@pytest.mark.smoke
def test_DELETE_METHOD_To_Delete_User_Account():
    email = "rohitjuyal111@gmail.com"
    password = "Rohitjuyal"
    response = DELETE_METHOD_To_Delete_User_Account_class.test_DELETE_METHOD_To_Delete_User_Account(email=email,password=password)
    print("Request Status",response.status_code)
    print("Request Text",response.text)
    assert response.status_code == 200,f"expected response 200 but got {response.status_code}"
    response_json = response.json()
    with open("Schemas/DELETE_METHOD_To_Delete_User_Account.json") as f:
        schema = json.load(f)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")
