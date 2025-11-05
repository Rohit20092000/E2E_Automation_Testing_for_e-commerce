import time
import os
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Utils.locators import Locators
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    TimeoutException,
)


def capture_screenshot(driver, screenshot_name, folder_name="capture_screenshot"):
    """
    Captures a screenshot and saves it to the given folder.
    """
    base_dir = os.getcwd()
    screenshot_dir = os.path.join(base_dir, folder_name)
    os.makedirs(screenshot_dir, exist_ok=True)

    # Add timestamp to avoid overwriting
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(screenshot_dir, f"{screenshot_name}_{timestamp}.png")

    driver.get_screenshot_as_file(file_path)
    print(f"✅ Screenshot saved at: {file_path}")

    return file_path



def safe_click(driver, xpath, timeout=30, retries=3):
    for attempt in range(retries):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )

            # Scroll element into view before clicking
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            element.click()
            return  # success → exit function

        except StaleElementReferenceException:
            print(f"[Retry {attempt+1}] Stale element, retrying...")
            time.sleep(2)

        except ElementClickInterceptedException:
            print(f"[Retry {attempt+1}] Click intercepted, trying to remove ad iframe...")
            try:
                ad_iframe = driver.find_element(By.CSS_SELECTOR, "iframe[id^='aswift']")
                driver.execute_script("arguments[0].remove();", ad_iframe)
                print("Ad iframe removed.")
            except:
                print("No ad iframe found to remove.")
            time.sleep(2)

        except TimeoutException:
            print("Timeout waiting for element to be clickable.")
            break

    raise Exception(f"safe_click failed after {retries} attempts for xpath: {xpath}")

def safe_send_keys(driver, xpath, value, timeout=30):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    ).send_keys(value)

def safe_get_text(driver, xpath, timeout=30):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    ).text


def safe_select(driver, xpath, value, by="text", timeout=30):
    for _ in range(3):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            select = Select(element)
            if value is None:

                return select.first_selected_option.text

            if by == "text":
                select.select_by_visible_text(value)
            elif by == "value":
                select.select_by_value(value)
            elif by == "index":
                select.select_by_index(int(value))
            return select.first_selected_option.text
        except StaleElementReferenceException:
            time.sleep(2)


def check_login_error(driver):
    error = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Locators.error_message)

    )
    assert error.is_displayed(), " Error message not shown for invalid login"
