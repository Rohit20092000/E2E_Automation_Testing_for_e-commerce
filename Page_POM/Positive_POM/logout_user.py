from Utils.selenium_helpers import safe_click, safe_get_text, safe_send_keys,safe_select
from Utils.locators import Locators
import allure

class Logout_user:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click on Signup / Login")
    def click_on_login(self):
        safe_click(self.driver,Locators.login)

    @allure.step("Enter your Email Id  {email} :")
    def email_filled(self,email):
        safe_send_keys(self.driver,Locators.sign_up_email,email)

    @allure.step("Enter your Password {password} :")
    def password_filled(self,password):
        safe_send_keys(self.driver,Locators.password,password)

    @allure.step("Click on Login Button :")
    def submission(self):
        safe_click(self.driver,Locators.submit)

    @allure.step("Click on Logout Button :")
    def logout_user(self):
        safe_click(self.driver,Locators.logout)