import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException,ElementNotSelectableException

@allure.title("This is an example for fluent explicit wait")
@allure.description("Verify that fluent explicit wait mechanism is works")
def test_fluent_explicit_wait_example():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    #<input type="email" class="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi">
    web_element_username = driver.find_element(By.ID, "login-username")
    web_element_username.send_keys("abc@gmail.com")

    #<input type="password" class="text-input W(100%)" name="password" id="login-password" data-qa="jobodapuxe">
    web_element_password = driver.find_element(By.NAME, "password")
    web_element_password.send_keys("12345")

    #<button id="js-sso-login-btn" type="submit" class="btn btn--positive btn--inverted" value="Sign in" onclick="login.loginUsingSSO(event)" data-qa="suregonici">
    web_element_sign_in = driver.find_element(By.ID, "js-login-btn")
    web_element_sign_in.click()

    #wait for sometime
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    (WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description"))))

    #<div class="notification-box-description" id="js-notification-box-msg" data-qa="rixawilomi">Your email, password, IP address or location did not match</div>
    web_element_text_message = driver.find_element(By.CLASS_NAME, "notification-box-description")
    assert web_element_text_message.text == "Your email, password, IP address or location did not match"

    driver.quit()
