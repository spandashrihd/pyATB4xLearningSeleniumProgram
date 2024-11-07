import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys


@allure.title("Actions Example 3")
@allure.description("Verify Mouse action click and hold")
def test_verify_actions_mouse_click_hold():
   driver = webdriver.Chrome()
   driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

   #draggable
   element_to_hold = driver.find_element(By.ID, "draggable")

   #click - normal driver , will find the element and click on it, release it.
   #click - hold - Action Chains - Click and Hold (don't release)

   time.sleep(2)


   actions = ActionChains(driver=driver)
   actions.click_and_hold(on_element=element_to_hold).perform()

   time.sleep(10)

