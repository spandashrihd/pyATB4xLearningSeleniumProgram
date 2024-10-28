from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pytest
import allure

@pytest.mark.negative
@allure.title("Verify Negative Testcase - app.vwo.com - Wrong Email/Password -Error Message.")
@allure.description("Verify that if email/password is wrong, we will et a message")
def test_negative_vwo_login_project2():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    #find an element-email
    #<input type="email" class="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi">
    web_element_username=driver.find_element(By.ID, "login-username")
    web_element_username.send_keys("abc@gmail.com")


    #find an element-password
    #<input type="password" class="text-input W(100%)" name="password" id="login-password" data-qa="jobodapuxe">
    #in this case class name is not unique bcz W(100), if we open this page in ipad its W(80), in our case class name change wit resolution
    web_element_password=driver.find_element(By.NAME,"password")
    web_element_password.send_keys("password@1234")

    #click on Sign in Button
    #<button id="js-sso-login-btn" type="submit" class="btn btn--positive btn--inverted" value="Sign in" onclick="login.loginUsingSSO(event)" data-qa="suregonici">
    web_element_signin_btn=driver.find_element(By.ID, "js-sso-login-btn")
    web_element_signin_btn.click()

    time.sleep(5)

    #verify that message is visible
    #<div class="notification-box-description" id="js-notification-box-msg" data-qa="rixawilomi">Your email, password, IP address or location did not match</div>
    web_element_message=driver.find_element(By.CLASS_NAME,"notification-box-description")
    assert web_element_message.text == "Your email, password, IP address or location did not match"

    time.sleep(5)
    driver.quit()


