import json

import pytest
from conftest import browserInstance
from Page_POM.Positive_POM.search import Search

test_data_path =r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
search_data = user_data["search_data"]
@pytest.mark.smoke
def test_register(browserInstance):
    browserInstance.get("https://automationexercise.com/")
    browserInstance.maximize_window()
    search_bar_check = Search(browserInstance)
    search_bar_check.click_on_product()
    search_bar_check.click_on_search()
    search_bar_check.send_data(user_data["search_data"])
    search_bar_check.click_on_search_bar()