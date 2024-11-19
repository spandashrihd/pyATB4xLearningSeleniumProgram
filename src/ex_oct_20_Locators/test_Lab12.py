from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Xpath example")
@allure.description("Verify that using XPath able to find en send keys to input")
def test_xpath_example():
   driver=webdriver.Chrome()
   driver.get("https://app.vwo.com/#/login")
   web_element_username=driver.find_element(By.XPATH, "//input[@id='login-username']")
   web_element_username.send_keys("abc@gmail.com")
   time.sleep(5)
   driver.quit()
