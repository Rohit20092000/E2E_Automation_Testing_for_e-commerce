import json
import time
import pytest
from Page_POM.Positive_POM.logout_user import Logout_user

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]


@pytest.mark.smoke
def test_register(browserInstance):
    browserInstance.get("https://automationexercise.com/")

    browserInstance.maximize_window()

    logout_user = Logout_user(browserInstance)
    logout_user.click_on_login()
    logout_user.email_filled(user_data["email"])
    logout_user.password_filled(user_data["password"])
    logout_user.submission()
    time.sleep(2)
    logout_user.logout_user()