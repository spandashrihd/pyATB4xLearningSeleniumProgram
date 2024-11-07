import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.

@allure.title("Actions Example")
@allure.description("Verify Actions")
def test_verify_actions_keyboard_event():
   driver = webdriver.Chrome()
   driver.get("https://awesomeqa.com/practice.html")

   #Xpath - //input[@name="firstname"]
   #css selector - input[name="firstname"]
   #By.name - firstname
   firstname = driver.find_element(By.XPATH, "//input[@name='firstname']")

   #shift key down
   actions = ActionChains(driver=driver)
   (actions.key_down(Keys.SHIFT).send_keys_to_element(firstname, "the testing academy").key_up(Keys.SHIFT).perform())

   time.sleep(10)
   driver.quit()
