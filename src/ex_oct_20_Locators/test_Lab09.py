from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pytest
import allure

@pytest.mark.positive
@allure.title("Positive Testcase - app.vwo.com start a free trail link verification")
@allure.description("Verify that Free Trail Button clicked, navigate to next page")
def test_positive_vwo_free_trial_project3():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    #find start a free trial element
    #<a href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage" class="text-link" data-qa="bericafeqo">Start a free trial</a>
    #LINK_TEXT = EXACT MATCH

    anchor_tag_element_link=driver.find_element(By.LINK_TEXT,"Start a free trial")
    anchor_tag_element_link.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    driver.back()   #go back to login page
    time.sleep(5)
    driver.quit()