import json

import pytest
from conftest import browserInstance
from Page_POM.Positive_POM.Verify_Test_Cases_Page import Verify_Test_cases_page

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]


@pytest.mark.smoke
def test_click_onTestcases(browserInstance):
    browserInstance.get("https://automationexercise.com/")
    browserInstance.maximize_window()
    click_on = Verify_Test_cases_page(browserInstance)
    click_on.click_on_Testcase()