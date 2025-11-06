from Utils.selenium_helpers import safe_click, safe_get_text, safe_send_keys,safe_select
from Utils.locators import Locators
import allure

class Correct_email:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click on Signup / Login")
    def login(self):
        safe_click(self.driver,Locators.login)

    @allure.step("Enter Your Email {email}")
    def Enter_email(self,email):
        safe_send_keys(self.driver,Locators.login_email,email)

    @allure.step("Enter Your Email {password}")
    def Enter_password(self,password):
        safe_send_keys(self.driver,Locators.password ,password)

    @allure.step("Click on Login Button")
    def submit_button(self):
        safe_click(self.driver,Locators.submit)

    @allure.step("Successfully_logged_in as Rohit Juyal")
    def Logged_in_shows(self):
        return safe_get_text(self.driver,Locators.successfully_logged_in)