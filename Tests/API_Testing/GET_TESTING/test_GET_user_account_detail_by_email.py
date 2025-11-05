import json
import pytest
import time
from API_CLIENTS.GET_API.GET_user_account_detail_by_email import GET_user_account_detail_by_email_class
from jsonschema import validate

@pytest.mark.smoke
def test_GET_user_account_detail_by_email_url():
    email = "rohitjuyal111@gmail.com"
    response = GET_user_account_detail_by_email_class.GET_user_account_detail_by_email(email= email)
    print("Response Status ", response.status_code)
    print("Response text :", response.text)
    assert response.status_code == 200,f"Expected 200, got {response.status_code}"