import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure

@pytest.mark.positive
@allure.title("Positive Testcase - app.vwo.com start a free trail link(partial link text) verification")
@allure.description("Verify that Free Trail Button clicked, navigate to next page using partial link text")
def test_positive_vwo_free_trial__partial_link_text_project3():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    #find start a free trial element
    #<a href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage" class="text-link" data-qa="bericafeqo">Start a free trial</a>
    #PARTIAL_LINK_TEXT = Contains

    anchor_tag_element_link=driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    anchor_tag_element_link.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    driver.back()   #go back to login page
    time.sleep(5)
    driver.quit()