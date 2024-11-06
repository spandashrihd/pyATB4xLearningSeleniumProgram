import time
from selenium import webdriver
import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@allure.title("Actions click and hold")
@allure.description("Verify click and hold actions")

def test_verify_spicejet_actions():
    driver=webdriver.Chrome()
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()

    from_city=driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep']")
    time.sleep(5)
    actions=ActionChains(driver)
    actions.move_to_element(from_city).click().send_keys("DEL").perform()
    time.sleep(10)