from Utils.locators import  Locators
from  Utils.selenium_helpers import safe_click
import allure

class Verify_Test_cases_page:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click on TestCase button to check it is visible or not: ")
    def click_on_Testcase(self):
        safe_click(self.driver,Locators.navigate_testcase)
