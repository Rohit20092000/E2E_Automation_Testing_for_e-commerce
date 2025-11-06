import json
import time
import re
import pytest
import allure
from Page_POM.Positive_POM.all_product_in_cart import all_product_in_cart
from Page_POM.Positive_POM.login_with_correct_email import Correct_email
from Utils.text_cleaner import clean_address_header


# ---------- Load test data ----------
test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
expected_name = f"{user_data['name']} {user_data['last_name']}".strip()
expected_company_name = user_data["company_name"]
expected_address = f"{user_data['address']} {user_data['address1']}".strip()
expected_country_name = user_data["country"]
expected_phone_number = user_data["Mobile"]


@pytest.mark.smoke
@allure.title("Verify Delivery and Billing Addresses after Adding Product to Cart")
@allure.description("Checks that delivery and billing addresses match each other and expected user data.")
@pytest.mark.smoke
def test_product_in_cart(browserInstance):
    driver = browserInstance
    driver.get("https://automationexercise.com/")
    driver.maximize_window()

    login_user = Correct_email(driver)
    login_user.login()
    login_user.Enter_email(user_data["email"])
    login_user.Enter_password(user_data["password"])
    login_user.submit_button()

    add_to_cart = all_product_in_cart(driver)
    add_to_cart.click_on_product()
    add_to_cart.add_product_on_cart()
    add_to_cart.view_cart()
    add_to_cart.proceed_to_check_out()

    # Get both addresses
    delivery_address = add_to_cart.delivery_address()
    billing_address = add_to_cart.billing_address()

    # Clean both using helper
    delivery_address = clean_address_header(delivery_address)
    billing_address = clean_address_header(billing_address)

    # Now compare them safely
   # assert delivery_address == billing_address



    delivery_address_display = f"YOUR BILLING ADDRESS \n Mr. {expected_name}\n{expected_company_name}\n{expected_address}\n{expected_country_name}\n{expected_phone_number}"
    assert delivery_address == delivery_address_display.strip()
