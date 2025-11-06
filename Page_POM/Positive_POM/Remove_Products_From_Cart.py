from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_select,safe_get_text,safe_send_keys
import allure

class remove_products_from_cart_class:

    def __init__(self,driver):
        self.driver = driver

    @allure.step("Add to cart :")
    def add_to_cart(self):
        safe_click(self.driver,Locators.add_first_product)

    @allure.step("View item in cart  :")
    def view_cart(self):
        safe_click(self.driver,Locators.view_cart)

    @allure.step("Remove item in cart  :")
    def remove_from_cart(self):
        safe_click(self.driver,Locators.remove_from_cart)

    @allure.step("Verify Item in cart  :")
    def verify_item_successfully_remove_from_cart(self):
        return safe_get_text(self.driver,Locators.cart_text_after_removing)
    def return_to_main_menu(self):
        safe_click(self.driver,Locators.return_from_cart)


