import time
import allure
from selenium  import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@allure.title("Drag and drop exercise")
@allure.description("Verify drag and drop functions")
def test_verify_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    #draggable element
    draggable_ele = driver.find_element(By.XPATH, "//div[@id='draggable']")

    #Droppable element
    drop_ele = driver.find_element(By.XPATH, "//div[@id='droppable']")

    #drag and drop actions
    ActionChains(driver).drag_and_drop(draggable_ele,drop_ele).perform()

    time.sleep(10)
    driver.quit()