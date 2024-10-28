from selenium import webdriver
import pytest
import allure

def test_verify_katalon_page():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    print(driver.title)
    page_source_data=driver.page_source
    assert 'CURA Healthcare Service' in page_source_data
    driver.quit()