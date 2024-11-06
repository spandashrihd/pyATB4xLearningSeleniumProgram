import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("practice buttons radio, checkbox")
@allure.description("Verify that able to click on buttons and checkbox")
def test_button_verification():
   driver = webdriver.Chrome()
   driver.get("https://awesomeqa.com/practice.html")

   firstname = driver.find_element(By.CSS_SELECTOR, "input[name='firstname']")
   firstname.send_keys("Spandashri")

   lastname = driver.find_element(By.CSS_SELECTOR, "input[name='lastname']")
   lastname.send_keys("Gowda")

   gender = driver.find_element(By.XPATH, "//input[@name='firstname']")
   gender.click()

   profession = driver.find_element(By.XPATH, "//input[@id='profession-1']")
   profession.click()

   time.sleep(10)
   driver.quit()
