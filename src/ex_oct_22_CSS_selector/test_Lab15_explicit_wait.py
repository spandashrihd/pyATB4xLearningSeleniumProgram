import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@allure.title("App.vwo.com - Explicit Wait")
@allure.description("Verify Explicit wait")
def test_explicit_wait_verification():
   driver = webdriver.Chrome()
   driver.get("https://app.vwo.com/#/login")
   web_element_username = driver.find_element(By.ID, "login-username")
   web_element_username.send_keys("abc@gmail.com")
   web_element_password = driver.find_element(By.NAME, "password")
   web_element_password.send_keys("12345")
   web_element_sign_in = driver.find_element(By.ID, "js-login-btn")
   web_element_sign_in.click()

   #Wait for sometime
   (WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description"))))
   web_element_text_message = driver.find_element(By.CLASS_NAME, "notification-box-description")
   assert web_element_text_message.text == "Your email, password, IP address or location did not match"
   print(web_element_text_message.text)
