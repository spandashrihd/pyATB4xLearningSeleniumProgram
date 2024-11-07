import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys


@allure.title("Actions Example ")
@allure.description("Verify Actions")
def test_verify_actions_mouse_back():
   driver = webdriver.Chrome()
   driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

   #click - normal driver , will find the element and click on it, release it.
   atag = driver.find_element(By.ID, "click")
   atag.click()

   time.sleep(5)

   #ActionBuilder for mouse
   actions_builders = ActionBuilder(driver=driver)
   actions_builders.pointer_action.pointer_up(MouseButton.BACK) #back, left, right, forward, backward etc
   actions_builders.perform()

   time.sleep(10)

