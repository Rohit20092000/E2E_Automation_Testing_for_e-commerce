from Utils.selenium_helpers import safe_click, safe_get_text, safe_send_keys, safe_select
from Utils.locators import Locators
import allure


class Register_user_with_existing_email:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click on Login Button")
    def sign_up_with_existing_user(self):
        safe_click(self.driver, Locators.login)

    @allure.step("Enter your First Name : {name}")
    def sign_up_with_existing_firstname(self, name):
        safe_send_keys(self.driver, Locators.sign_up_name, name)

    @allure.step("Enter your Last Name : {last_name}")
    def sign_up_with_existing_lastname(self, last_name):
        safe_send_keys(self.driver, Locators.sign_up_name, last_name)

    @allure.step("Enter your Email ID : {email}")
    def sign_up_with_existing_emailID(self, email):
        safe_send_keys(self.driver, Locators.sign_up_email, email)

    @allure.step("Click on Submit button")
    def click_on_submit_button(self):
        safe_click(self.driver, Locators.sign_up_button)

    @allure.step("Error Message Displayed on Website")
    def existed_message(self):
        existing_email_message_1 = safe_get_text(self.driver, Locators.existing_email_message)
        return existing_email_message_1
