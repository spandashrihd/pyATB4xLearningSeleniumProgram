from selenium import webdriver
import allure
import pytest


@allure.title("verify the Title of app.vwo.com")
def test_open_vwo_login():
    driver=webdriver.Chrome()
    #POST request to create a new fresh copy of Chrome
    #Fresh - Chrome -Session ID

    driver.get("https://app.vwo.com")
    #Code - HTTP request - Chromedriver(selenium manager) - chrome(session id)
    print(driver.title)  #GET request
    assert driver.title == "Login - VWO"