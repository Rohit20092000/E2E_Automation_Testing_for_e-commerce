import json
import time
import pytest
from Page_POM.Positive_POM.delete_account import Delete_Account
from Page_POM.Positive_POM.login_with_correct_email import Correct_email

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]


@pytest.mark.smoke
def test_correct_email(browserInstance):
    browserInstance.get("https://automationexercise.com/")

    browserInstance.maximize_window()
    login_user = Correct_email(browserInstance)
    login_user.login()
    login_user.Enter_email(user_data["email"])
    login_user.Enter_password(user_data["password"])
    login_user.submit_button()
    time.sleep(2)
    delete_account = Delete_Account(browserInstance)

    delete_account.delete_account_1()
