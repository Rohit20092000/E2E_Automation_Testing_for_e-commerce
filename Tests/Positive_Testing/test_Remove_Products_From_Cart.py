from Page_POM.Positive_POM.Remove_Products_From_Cart import remove_products_from_cart_class
import pytest
import time
import json
from Page_POM.Positive_POM.login_with_correct_email import Correct_email



test_data_path =r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]
user_data = test_list[0]
search_data = user_data["search_data"]
@pytest.mark.smoke
def test_remove_products_from_cart(browserInstance):
    browserInstance.get("http://automationexercise.com")
    browserInstance.maximize_window()
    login_with_correct_email = Correct_email(browserInstance)
    login_with_correct_email.login()
    login_with_correct_email.Enter_email(user_data["email"])
    login_with_correct_email.Enter_password(user_data["password"])
    login_with_correct_email.submit_button()
    Remove_product = remove_products_from_cart_class(browserInstance)
    Remove_product.add_to_cart()
    Remove_product.view_cart()
    Remove_product.remove_from_cart()
    time.sleep(2)
    empty_cart_message = "Cart is empty! Click here to buy products."
    assert empty_cart_message == Remove_product.verify_item_successfully_remove_from_cart()
    time.sleep(12)
    Remove_product.return_to_main_menu()
    time.sleep(3)

