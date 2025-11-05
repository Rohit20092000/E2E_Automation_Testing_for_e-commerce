
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_get_text,safe_send_keys,safe_select
import allure

class download_invoice:
    def __init__(self,driver):
        self.driver = driver
    @allure.step("Scrap the first product price")
    def first_product(self):
        return safe_get_text(self.driver,Locators.first_product)
    @allure.step(" Scrap the Second product price : ")
    def second_product(self):
        return safe_get_text(self.driver,Locators.second_product)
    @allure.step(" Total price : ")
    def total_price(self):
        return safe_get_text(self.driver,Locators.total_price)
    @allure.step("You may input message to the delivery partner {user_comment} : ")
    def enter_message(self,user_comment):
        safe_send_keys(self.driver,Locators.comment,user_comment)
    @allure.step("Place order : ")
    def place_order(self):
        safe_click(self.driver,Locators.place_order)

    @allure.step("Card Name {name} : ")
    def card_first_name(self,name):
        safe_send_keys(self.driver,Locators.card_name,name)

    @allure.step("Card Name {last_name} : ")
    def card_second_name(self, last_name):
        safe_send_keys(self.driver, Locators.card_name,last_name)
    @allure.step("card number : {card_number}")
    def card_number(self,card_number):
        safe_send_keys(self.driver,Locators.card_number,card_number)
    @allure.step("Enter csv number {csv} : ")
    def card_csv(self,csv):
        safe_send_keys(self.driver,Locators.cvc,csv)
    @allure.step("Enter Card expire month {expire_month} ")
    def expire_month(self,expire_month):
        safe_send_keys(self.driver,Locators.card_expire_month,expire_month)
    @allure.step(" Enter Card expire year {expire_year} ")
    def expire_year(self,expire_year):
        safe_send_keys(self.driver,Locators.card_expire_year,expire_year)

    @allure.step(" Click on place order ")
    def pay_and_confirm_order(self):
        safe_click(self.driver,Locators.submit_card_details)

    @allure.step(" Click on download button ")
    def click_on_download_invoice(self):
        safe_click(self.driver,Locators.download_invoice)