import time

from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("List all the buttons by using TAG_NAME")
@allure.description("Verify that all buttons are printing using TAG_NAME")
def test_tag_name_verification():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    #find all the buttons in the page
    buttons=driver.find_elements(By.TAG_NAME, "button")
    print(len(buttons))
    for i in buttons:
        print(i.text)

    #find all the links in the page
    all_links=driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links))
    for i in all_links:
        print(i.text)

    time.sleep(5)
    driver.quit()
