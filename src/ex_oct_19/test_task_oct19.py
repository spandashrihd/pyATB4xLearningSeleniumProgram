from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("Automation for the Registration Page of the AwesomeQA.com/UI")
@allure.description("Verify that next page give - Your Account Has Been Created!")
def test_registration_page_automation():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    #Finding "first name" web element
    #<input type="text" name="firstname" value="" placeholder="First Name" id="input-firstname" class="form-control">
    web_element_firstname=driver.find_element(By.ID, "input-firstname")
    web_element_firstname.send_keys("Spandashri")

    # Finding "last name" web element
    # <input type="text" name="lastname" value="" placeholder="Last Name" id="input-lastname" class="form-control">
    web_element_lastname = driver.find_element(By.ID, "input-lastname")
    web_element_lastname.send_keys("Gowda")

    #Finding "E-mail" web element
    #<input type="email" name="email" value="" placeholder="E-Mail" id="input-email" class="form-control">
    web_element_email = driver.find_element(By.NAME, "email")
    web_element_email.send_keys("sfplknjbftdxc@gmail.com")

    # Finding "Telephone" web element
    #<input type="tel" name="telephone" value="" placeholder="Telephone" id="input-telephone" class="form-control">
    web_element_telephone = driver.find_element(By.NAME, "telephone")
    web_element_telephone.send_keys("9876543210")

    # Finding "password" web element
    # <input type="password" name="password" value="" placeholder="Password" id="input-password" class="form-control">
    web_element_password = driver.find_element(By.ID, "input-password")
    web_element_password.send_keys("pass@123")

    # Finding "password confirm" web element
    # <input type="password" name="confirm" value="" placeholder="Password Confirm" id="input-confirm" class="form-control">
    web_element_password_confirm = driver.find_element(By.ID, "input-confirm")
    web_element_password_confirm.send_keys("pass@123")

    #finding "checkbox" web element
    #<input type="checkbox" name="agree" value="1">
    web_element_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    web_element_checkbox.click()

    #finding "continue" we element
    #<input type="submit" value="Continue" class="btn btn-primary">
    web_element_submit_btn = driver.find_element(By.XPATH,"//input[@value='Continue']")
    web_element_submit_btn.click()

    time.sleep(10)
    assert "Your Account Has Been Created!" in driver.page_source
    driver.quit()




