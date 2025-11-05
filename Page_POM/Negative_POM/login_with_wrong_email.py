from Utils.selenium_helpers import safe_click, safe_get_text, safe_send_keys,safe_select
from Utils.locators import Locators
import allure

class Wrong_email:
    def __init__(self, driver):
        self.driver = driver
    @allure.step("Click on Signup / Login :")
    def login(self):
        safe_click(self.driver,Locators.login)

    @allure.step("Enter Wrong Email Id to Check {email} :")
    def send_email(self,email):
        safe_send_keys(self.driver,Locators.login_email,email)

    @allure.step("Enter Wrong Password to Check {wrong_password} :")
    def send_password(self,wrong_password):
        safe_send_keys(self.driver,Locators.password,wrong_password)

    @allure.step("Click on Submit :")
    def submit(self):
        safe_click(self.driver, Locators.submit)

    @allure.step("Capture ScreenShot to Debug:")
    def capture_result_screenshot(self, filename="error.png"):
        self.driver.get_screenshot_as_file(filename)

    @allure.step("Check Error Message")
    def error_message(self):
        error_message = safe_get_text(self.driver,Locators.error_message)
        return error_message

