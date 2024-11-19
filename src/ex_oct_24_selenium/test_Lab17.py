import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@allure.title("Alerts example")
@allure.description("Verify Alerts")
def test_alerts_js_alert_verification():
   driver = webdriver.Chrome()
   driver.get("https://the-internet.herokuapp.com/javascript_alerts ")
   driver.maximize_window()
   #Click on the Alert button and check the Result - (Assertion of the result)
   #//button[@onclick = "jsAlert()"]
   #id="result"

   element_prompt=driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
   element_prompt.click()

   WebDriverWait(driver=driver, timeout=5).until((EC.alert_is_present()))

   alert=driver.switch_to.alert
   alert.accept()

   result_text=driver.find_element(By.ID, "result").text
   assert result_text == "You successfully clicked an alert"

   time.sleep(5)

def test_alerts_confirm_verification():
   driver = webdriver.Chrome()
   driver.get("https://the-internet.herokuapp.com/javascript_alerts ")
   driver.maximize_window()
   #Click on the Alert button and check the Result - (Assertion of the result)
   #//button[@onclick = "jsAlert()"]
   #id="result"

   element_confirm=driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
   element_confirm.click()

   WebDriverWait(driver=driver, timeout=5).until((EC.alert_is_present()))

   alert=driver.switch_to.alert
   alert.dismiss()

   result_text=driver.find_element(By.ID, "result").text
   assert result_text == "You clicked: Cancel"

   time.sleep(5)

def test_alerts_prompt_verification():
   driver = webdriver.Chrome()
   driver.get("https://the-internet.herokuapp.com/javascript_alerts ")

   #Click on the Alert button and check the Result - (Assertion of the result)
   #//button[@onclick = "jsAlert()"]
   #id="result"

   element_prompt=driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
   element_prompt.click()

   WebDriverWait(driver=driver, timeout=5).until((EC.alert_is_present()))

   alert=driver.switch_to.alert
   alert.send_keys("Spanda")
   alert.accept()
   #alert.dismiss()

   result_text=driver.find_element(By.ID, "result").text
   assert result_text == "You clicked: Spanda"

   time.sleep(5)