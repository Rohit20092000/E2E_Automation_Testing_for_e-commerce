from Page_POM.Positive_POM.Download_Invoice_after_purchase_order import download_invoice
from Page_POM.Positive_POM.login_with_correct_email import Correct_email
from Page_POM.Positive_POM.all_product_in_cart import all_product_in_cart
import time
import pytest
import json

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]


@pytest.mark.smoke
def test_order_complete(browserInstance):
    driver = browserInstance
    browserInstance.get("https://automationexercise.com/")
    browserInstance.maximize_window()
    login_user = Correct_email(browserInstance)
    login_user.login()
    login_user.Enter_email(user_data["email"])
    login_user.Enter_password(user_data["password"])
    login_user.submit_button()
    time.sleep(2)
    add_product_in_your_cart = all_product_in_cart(browserInstance)
    add_product_in_your_cart.click_on_product()
    add_product_in_your_cart.add_product_on_cart()
    add_product_in_your_cart.view_cart()
    add_product_in_your_cart.proceed_to_check_out()
    add_product_in_your_cart.delivery_address()
    complete_order = download_invoice(browserInstance)
    First_product = complete_order.first_product()
    Second_product = complete_order.second_product()
    Total_price_on_web = complete_order.total_price()
    Total_Price = First_product + Second_product
    print(Total_Price)
    time.sleep(3)
    # assert Total_price_on_web == Total_Price
    complete_order.enter_message(user_data["comment"])
    complete_order.place_order()
    complete_order.card_first_name(user_data["name"])
    complete_order.card_second_name(user_data["last_name"])
    complete_order.card_number(user_data["card_number"])
    complete_order.card_csv(user_data["csv"])
    complete_order.expire_month(user_data["expire_month"])
    complete_order.expire_year(user_data["expire_year"])
    complete_order.pay_and_confirm_order()
    time.sleep(2)
    complete_order.click_on_download_invoice()
    time.sleep(1)

