from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_get_text,safe_send_keys,safe_select
import allure


class all_product_in_cart:

    def __init__(self,driver):
        self.driver = driver

    @allure.step("Click on the Product Button : ")
    def click_on_product(self):
        safe_click(self.driver, Locators.products)

    @allure.step("Adding product on cart : ")
    def add_product_on_cart(self):
        safe_click(self.driver, Locators.add_first_product)

    @allure.step("View product on cart : ")
    def view_cart(self):
        safe_click(self.driver, Locators.view_cart)

    @allure.step("Proceed to checkout : ")
    def proceed_to_check_out(self):
        safe_click(self.driver, Locators.proceed)

    @allure.step("Your Delivery address : ")
    def delivery_address(self):
        return safe_get_text(self.driver, Locators.d_address)

    @allure.step("Your billing address : ")
    def billing_address(self):
        return safe_get_text(self.driver, Locators.b_address)


