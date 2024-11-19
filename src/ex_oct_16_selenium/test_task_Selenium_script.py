from selenium import webdriver
import pytest
import allure

@allure.title("Verify title and Current URL of web page")
def test_open_katalon():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    print(driver.title)

    #Verify with asserstions
    assert driver.title == "CURA Healthcare Service"
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    assert driver.page_source.__contains__("CURA Healthcare Service")