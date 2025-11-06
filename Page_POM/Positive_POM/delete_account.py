from Utils.selenium_helpers import safe_click, safe_get_text, safe_send_keys,safe_select
from Utils.locators import Locators
import allure

class Delete_Account:
    def __init__(self,driver):
        self.driver = driver

    @allure.step("Click on Delete Account to Delete User Name :")
    def delete_account_1(self):
        safe_click(self.driver,Locators.delete_account)

