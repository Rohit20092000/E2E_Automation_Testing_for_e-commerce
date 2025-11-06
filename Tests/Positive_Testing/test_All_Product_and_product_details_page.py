import json
import pytest
from Page_POM.Positive_POM.Verify_All_Products_and_product_detail_page import Products_and_product_detail_page

test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\E2E_Automation_Testing_for_e-commerce\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]




@pytest.mark.smoke
def test_register(browserInstance):
    browserInstance.get("https://automationexercise.com/")
    browserInstance.maximize_window()
    all_product_checks = Products_and_product_detail_page(browserInstance)
    all_product_checks.click_on_product()
    all_product_checks.click_on_women()
    all_product_checks.click_on_dress()
    dress_text = all_product_checks.women_dress_text()
    display_text = f"WOMEN - DRESS PRODUCTS"
    print(dress_text)
    print(display_text)
    assert dress_text == display_text.strip()
    all_product_checks.click_on_women()
    all_product_checks.click_on_top()
    women_top_text = all_product_checks.women_top_text()
    display_text_1 = f"WOMEN - TOPS PRODUCTS"
    print(women_top_text)
    print(display_text_1)
    assert women_top_text == display_text_1.strip()

    all_product_checks.click_on_women()
    all_product_checks.click_on_saree()
    women_saree_text  = all_product_checks.women_saree_text()
    display_text_2 = f"WOMEN - SAREE PRODUCTS"
    print(women_saree_text)
    print(display_text_2)
    assert women_saree_text == display_text_2.strip()
    #men section
    all_product_checks.click_on_men_section()
    all_product_checks.men_tshirt()
    men_tshirt_text = all_product_checks.tshirt_text()
    men_display = f"MEN - TSHIRTS PRODUCTS"
    print(men_display)
    print(men_tshirt_text)
    assert men_tshirt_text == men_display.strip()
    all_product_checks.click_on_men_section()
    all_product_checks.clck_on_jeans()
    men_jeans_text = all_product_checks.jeans_text()
    men_jeans_text_1 = f"MEN - JEANS PRODUCTS"
    print(men_jeans_text)
    print(men_jeans_text_1)
    assert men_jeans_text == men_jeans_text_1.strip()
    #Kid Section
    all_product_checks.click_on_kids()
    all_product_checks.click_on_kids_dress()
    kids_dress = all_product_checks.text_on_kids_dress()
    kids_dress_display = f"KIDS - DRESS PRODUCTS"
    assert kids_dress == kids_dress_display.strip()
    all_product_checks.click_on_kids()
    all_product_checks.click_on_Tops_Shirts()
    kids_tops_shirts = all_product_checks.text_on_Tops_Shirts()
    kids_tops_shirts_display = f"KIDS - TOPS & SHIRTS PRODUCTS" #Tops & Shirts
    assert kids_tops_shirts == kids_tops_shirts_display.strip()

