from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_get_text,safe_send_keys
import allure
class Search:
    def __init__(self,driver):
        self.driver = driver

    @allure.step("Click on the Product Button : ")
    def click_on_product(self):
        safe_click(self.driver,Locators.products)

    @allure.step("Click on the Search Bar : ")
    def click_on_search(self):
        safe_click(self.driver,Locators.search)

    @allure.step("Enter Product Name to Search Item {search_data} : ")
    def send_data(self,search_data):
        safe_send_keys(self.driver,Locators.search,search_data)

    @allure.step("Click on the Search Bar Icon to Search Product : ")
    def click_on_search_bar(self):
        safe_click(self.driver,Locators.search_click)
