import json
import time

import pytest

from Page_POM.Negative_POM.login_with_wrong_email import Wrong_email

from Utils.selenium_helpers import capture_screenshot

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["wrong_data"]

user_data = test_list[0]


@pytest.mark.smoke
def test_wrong_email(browserInstance):
    browserInstance.get("https://automationexercise.com/")
    browserInstance.maximize_window()
    login_with_wrong_email = Wrong_email(browserInstance)
    login_with_wrong_email.login()
    login_with_wrong_email.send_email(user_data["email"])
    login_with_wrong_email.send_password(user_data["wrong_password"])
    login_with_wrong_email.submit()
    capture_screenshot(browserInstance, "error.png")

    error_message = login_with_wrong_email.error_message()
    print(error_message)  # Debugging output

    assert error_message == "Your email or password is incorrect!", \
        f"Expected 'Your email or password is incorrect!' but got: {error_message}"

    time.sleep(1)