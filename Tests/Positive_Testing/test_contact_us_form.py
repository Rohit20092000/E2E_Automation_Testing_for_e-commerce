import json
import pytest
from Page_POM.Positive_POM.Contact_Us_Form import Contact_us

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]


@pytest.mark.smoke
def test_register(browserInstance):
    browserInstance.get("https://automationexercise.com/")

    browserInstance.maximize_window()
    contact_page = Contact_us(browserInstance)
    contact_page.click_contact_button()

