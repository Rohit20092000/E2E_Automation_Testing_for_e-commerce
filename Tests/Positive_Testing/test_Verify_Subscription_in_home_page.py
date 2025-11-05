from Page_POM.Positive_POM.Verify_Subscription_in_home_page import Subscription
import json
import pytest
from conftest import browserInstance

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
search_data = user_data["search_data"]
@pytest.mark.smoke
def test_subscription(browserInstance):
    browserInstance.get("https://automationexercise.com/")
    browserInstance.maximize_window()
    subscription_check = Subscription(browserInstance)
    subscription_check.scroll_down()
    subscription_check.click_on_box()
    subscription_check.send_data(user_data["email"])
    subscription_check.click_on_subscription_button()
    alert_message_display = subscription_check.alert_message()
    assert alert_message_display == "You have been successfully subscribed!"