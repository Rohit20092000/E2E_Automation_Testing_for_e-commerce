from Utils.selenium_helpers import safe_click, safe_get_text, safe_send_keys,safe_select
from Utils.locators import Locators
import allure


class register:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click on Signup / Login")
    def Click_on_Signup_Login(self):
        safe_click(self.driver,Locators.login)

    @allure.step("Enter First Name {name} ")
    def sign_up_first_name(self,name):
        safe_send_keys(self.driver,Locators.sign_up_name,name)

    @allure.step("Enter Last Name :{last_name} ")
    def sign_up_last_name(self,last_name):
        safe_send_keys(self.driver,Locators.sign_up_name,last_name)

    @allure.step("Enter Email for SignUp :{email} ")
    def sign_up_email(self,email):
        safe_send_keys(self.driver,Locators.sign_up_email,email)

    @allure.step("Click On Sign Up Button ")
    def sign_up_button_click(self):
        safe_click(self.driver,Locators.sign_up_button)

    @allure.step("Click On Sign Up Button ")
    def select_title(self):
        safe_click(self.driver,Locators.title)

    @allure.step("Enter Password {password} ")
    def enter_password(self,password):
        safe_send_keys(self.driver,Locators.password,password)

    @allure.step("Select Day {day} ")
    def select_day(self, day):
        safe_select(self.driver,Locators.days,day)

    @allure.step("Select Day {month} ")
    def select_month(self,month):
        safe_select(self.driver,Locators.month_select,month)

    @allure.step("Select Day {year} ")
    def select_year(self,year):
        safe_select(self.driver,Locators.year_select ,year)

    @allure.step("Select Sign up for our newsletter! ")
    def select_sign_up(self):
         safe_click(self.driver,Locators.checkbox_1)

    @allure.step("Receive special offers from our partners!")
    def select_receive_special_offer(self):
        safe_click(self.driver,Locators.checkbox_2)

    @allure.step("Enter First Name {name}")
    def Enter_first_name(self,name):
        safe_send_keys(self.driver,Locators.add_name,name)

    @allure.step("Enter Last Name {last_name}")
    def Enter_user_last_name(self,last_name):
        safe_send_keys(self.driver,Locators.last_name,last_name)

    @allure.step("Enter Company Name {company_name}")
    def Enter_company_name(self,company_name):
        safe_send_keys(self.driver,Locators.company_name ,company_name)

    @allure.step("Enter First Address {address}")
    def Enter_address(self, address):
        safe_send_keys(self.driver, Locators.address, address)

    @allure.step("Enter Second Address {address1}")
    def Enter_address_1(self, address1):
        safe_send_keys(self.driver, Locators.address_2, address1)

    @allure.step("Select Country Name {country}")
    def select_country(self,country):
        safe_select(self.driver,Locators.country,country)

    @allure.step("Enter State Name {state}")
    def Enter_state(self,state):
        safe_send_keys(self.driver, Locators.state_name,state)

    @allure.step("Enter City Name {city}")
    def Enter_city(self,city):
        safe_send_keys(self.driver,Locators.city_name,city)

    @allure.step("Enter your Zip-Code {zip_code}")
    def Enter_zip_code(self,zip_code):
        safe_send_keys(self.driver,Locators.zip_code,zip_code)

    @allure.step("Enter your Mobile Number {Mobile}")
    def mobile_number(self, Mobile):
        safe_send_keys(self.driver, Locators.Mobile_number, Mobile)

    @allure.step("Enter your Mobile Number {create_account_button}")
    def click_on_submit(self):
        safe_click(self.driver,Locators.create_account_button)

    @allure.step("Message display on Website after Account Successfully Created")
    def account_creation_message(self):
        return safe_get_text(self.driver,Locators.Account_creation_message)

    @allure.step("Click on Continue Button after account created")
    def continue1(self):
        safe_click(self.driver,Locators.continue_button)






