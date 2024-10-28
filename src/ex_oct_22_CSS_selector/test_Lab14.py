from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("This is an example for implicit wait")
@allure.description("Verify that implicit wait will be applied")
def test_implicit_wait_example():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    web_element_username=driver.find_element(By.XPATH, "//input[@id='login-username']")
    web_element_username.send_keys("abc@gmail.com")

    #adding implicit wait
    driver.implicitly_wait(5)
    driver.quit()