import json
import time

import pytest
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_get_text
from Page_POM.Positive_POM.Register_User import register

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
    registration= register(browserInstance)
    registration.Click_on_Signup_Login()

    registration.sign_up_first_name(user_data["name"])
    registration.sign_up_last_name(user_data["last_name"])
    registration.sign_up_email(user_data["email"])
    registration.sign_up_button_click()
    registration.select_title()
    registration.enter_password(user_data["password"])
    registration.select_day(user_data["day"])
    registration.select_month(user_data["month"])
    registration.select_year(user_data["year"])
    registration.select_sign_up()
    registration.select_receive_special_offer()
    registration.Enter_first_name(user_data["name"])
    registration.Enter_user_last_name(user_data["last_name"])
    registration.Enter_company_name(user_data["company_name"])
    registration.Enter_address(user_data["address"])
    registration.Enter_address_1(user_data["address1"])
    registration.select_country(user_data["country"])
    registration.Enter_state(user_data["state"])
    registration.Enter_city (user_data["city"])
    registration.Enter_zip_code(user_data["zip_code"])
    registration.mobile_number(user_data["Mobile"])
    safe_click(browserInstance,Locators.create_account_button)
    text = safe_get_text(browserInstance, Locators.Account_creation_message)
    print(f"contact: {text}")
    Account_creation_message = safe_get_text(browserInstance, Locators.Account_creation_message)
    assert Account_creation_message.strip() == text.strip(), f"Expected '{Account_creation_message}' but got '{text}'"
    time.sleep(30)
    registration.continue1()
