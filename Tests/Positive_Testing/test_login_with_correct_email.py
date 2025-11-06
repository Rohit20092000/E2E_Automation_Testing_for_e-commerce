import json
import time
import pytest
from Page_POM.Positive_POM.login_with_correct_email import Correct_email

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
expected_first_name = user_data["name"]
expected_last_name = user_data["last_name"]

@pytest.mark.smoke
def test_correct_email(browserInstance):
    browserInstance.get("https://automationexercise.com/")

    browserInstance.maximize_window()
    login_with_correct_email = Correct_email(browserInstance)
    login_with_correct_email.login()
    login_with_correct_email.Enter_email(user_data["email"])
    login_with_correct_email.Enter_password(user_data["password"])
    login_with_correct_email.submit_button()
    console_message = login_with_correct_email.Logged_in_shows()
    print(console_message)
    display_message = f" Logged in as {expected_first_name}{expected_last_name}"

    assert console_message.strip() == display_message.strip(), \
        f"Expected '{console_message}' but got: '{display_message}'"
    time.sleep(10)