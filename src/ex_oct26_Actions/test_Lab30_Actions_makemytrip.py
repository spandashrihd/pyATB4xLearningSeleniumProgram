import time
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@allure.title("Actions makemytrip.com automate")
@allure.description("Verify actions makemytrip")
def test_verify_makemytrip_actions():
   #Chrome oprions --> --incoginito
   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_argument("--incognito")
   driver = webdriver.Chrome()
   driver.get("https://www.makemytrip.com/")

   #//span[@data-cy="closeModal"] --> wait --> click
   WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']")))

   driver.find_element(By.XPATH, "//span[@data-cy='closeModal']").click()

   time.sleep(2)

   fromCity = driver.find_element(By.ID, "fromCity")
   #Move the mouse to fromCity -input box
   #click on it
   #DEL enter
   #Arrow - select first one (up and down)
   #Enter

   actions = ActionChains(driver)
   (actions.move_to_element(fromCity).click().send_keys("del").perform())    #after entering del, wait for sometime to popup options

   time.sleep(2)

   (actions.move_to_element(fromCity).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform())

   time.sleep(10)
   driver.quit()