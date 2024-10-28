import time
import allure
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By


@allure.title("Handling Stale Exceptions")
@allure.description("Verify stale Exceptions handles")
def test_handle_stale_exception_verification():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    try:
        text_area = driver.find_element(By.NAME, "q")
        driver.refresh()
        text_area.send_keys("The Testing Academy")
    except StaleElementReferenceException as ser:
        print(ser.msg)
        print("stale element reference")

    time.sleep(5)