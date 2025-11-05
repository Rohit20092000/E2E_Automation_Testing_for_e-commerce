from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_send_keys,safe_get_text
import allure
class Subscription:

    def __init__(self,driver):
        self.driver = driver

    @allure.step("Scroll Page  : ")
    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

    @allure.step("Click on Box to Check Subscription : ")
    def click_on_box(self):

        safe_click(self.driver,Locators.subscription)

    @allure.step("Enter your mail id to check {email}: ")
    def send_data(self,email):
        safe_send_keys(self.driver,Locators.subscription,email)

    @allure.step("Click on Subscription button: ")
    def click_on_subscription_button(self):
        safe_click(self.driver,Locators.subscription_submit)

    @allure.step("Alert message will be shown ")
    def alert_message(self):
        return safe_get_text(self.driver,Locators.temporary)






