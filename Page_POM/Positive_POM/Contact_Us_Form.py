from Utils.selenium_helpers import safe_click, safe_get_text, safe_send_keys,safe_select
from Utils.locators import Locators
from selenium.webdriver.common.by import By

class Contact_us:
    def __init__(self, driver):
        self.driver = driver
    def click_contact_button(self):
        safe_click(self.driver,Locators.contact_us)