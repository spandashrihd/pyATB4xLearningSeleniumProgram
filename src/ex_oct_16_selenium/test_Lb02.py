from selenium import webdriver
import pytest
import allure

@allure.title("Verify the current url of the web page google.com")
def test_sample():
    driver=webdriver.Edge()
    driver.get("https://google.com")
    assert driver.current_url == "https://www.google.com/"