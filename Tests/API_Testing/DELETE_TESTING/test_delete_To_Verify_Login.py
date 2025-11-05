import json
import pytest
from jsonschema import validate
from API_CLIENTS.DELETE_API.DELETE_To_Verify_Login import DELETE_To_Verify_Login_class


@pytest.mark.smoke
def test_DELETE_To_Verify_Login_class():
    response = DELETE_To_Verify_Login_class.DELETE_To_Verify_Login()
    print("Status code ",response.status_code)
    print("Response body",response.text)
