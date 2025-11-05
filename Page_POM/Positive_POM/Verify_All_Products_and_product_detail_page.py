from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_get_text,safe_send_keys,safe_select
import allure

class Products_and_product_detail_page:
    def __init__(self,driver):
        self.driver = driver

    @allure.step("Click on the Product Button : ")
    def click_on_product(self):
        safe_click(self.driver,Locators.products)
    @allure.step("Click on the Women button? : ")
    def click_on_women(self):
        safe_click(self.driver,Locators.women)

    @allure.step("Click on the Dress : ")
    def click_on_dress(self):
        safe_click(self.driver,Locators.dress)

    @allure.step(" Dress Text is visible : ")
    def women_dress_text(self):
        return safe_get_text(self.driver,Locators.dress_text)

    @allure.step("Click on the Top :")
    def click_on_top(self):
        safe_click(self.driver,Locators.top)

    @allure.step("Top Text is visible : ")
    def women_top_text(self):
        return safe_get_text(self.driver,Locators.top_text)

    @allure.step("Click on the Top : ")
    def click_on_saree(self):
        safe_click(self.driver,Locators.saree)

    @allure.step(" Saree Text is visible")
    def women_saree_text(self):
        return safe_get_text(self.driver,Locators.saree_text)
    #Women Section is completed
    @allure.step("Click on the Men : ")
    def click_on_men_section(self):
        safe_click(self.driver,Locators.men)

    @allure.step("Click on the Tshirt : ")
    def men_tshirt(self):
        safe_click(self.driver,Locators.tshirt)

    @allure.step("Tshirt Page will be open , and Text will be visible : ")
    def tshirt_text(self):
        return safe_get_text(self.driver,Locators.tshirt_text)

    @allure.step("Click on the Jeans : ")
    def clck_on_jeans(self):
        safe_click(self.driver,Locators.jeans)

    @allure.step("Jeans Page will be open , and Text will be visible : ")
    def jeans_text(self):
        return safe_get_text(self.driver,Locators.jeans_text)

    #Men section is finished
    @allure.step("Click on the Kids : ")
    def click_on_kids(self):
        safe_click(self.driver,Locators.kids)

    @allure.step("Click on the Kid Dress : ")
    def click_on_kids_dress(self):
        safe_click(self.driver, Locators.kids_dress)

    @allure.step("Kids Page will be open , and Text will be visible ")
    def text_on_kids_dress(self):
        return safe_get_text(self.driver,Locators.kids_dress_text)

    @allure.step("Click on the Tops_Shirts : ")
    def click_on_Tops_Shirts(self):
        safe_click(self.driver,Locators.Tops_Shirts)

    @allure.step("Tops_Shirts Page will be open , and Text will be visible ")
    def text_on_Tops_Shirts(self):
        return safe_get_text(self.driver,Locators.Tops_Shirts_text)



