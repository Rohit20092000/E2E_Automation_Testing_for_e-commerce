import json
import time
import pytest
from Page_POM.Negative_POM.register_user_with_existing_email import Register_user_with_existing_email

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]

@pytest.mark.smoke
def test_register(browserInstance):
    driver = browserInstance
    browserInstance.get("https://automationexercise.com/")
    browserInstance.maximize_window()
    signup_check_with_existing_user = Register_user_with_existing_email(browserInstance)
    signup_check_with_existing_user.sign_up_with_existing_user()

    signup_check_with_existing_user.sign_up_with_existing_firstname(user_data["name"])
    signup_check_with_existing_user.sign_up_with_existing_lastname(user_data["last_name"])
    signup_check_with_existing_user.sign_up_with_existing_emailID(user_data["email"])
    signup_check_with_existing_user.click_on_submit_button()
    existing_email_message = signup_check_with_existing_user.existed_message()
    print(existing_email_message)  # Debugging output

    assert existing_email_message == "Email Address already exist!", \
        f"Expected 'Email Address already exist!' but got: {existing_email_message}"

    time.sleep(12)