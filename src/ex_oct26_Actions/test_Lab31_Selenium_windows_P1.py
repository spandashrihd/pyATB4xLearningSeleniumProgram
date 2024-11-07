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


@allure.title("windows P1")
@allure.description("Verify windows")
def  test_verify_windows():
   #Chrome oprions --> --incoginito
   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_argument("--incognito")

   driver = webdriver.Chrome()
   driver.get("https://the-internet.herokuapp.com/windows")
   driver.maximize_window()
   
   #parent windows #1
   parent_window = driver.current_window_handle
   print(parent_window)

   #<a href="/windows/new" ,="" target="_blank">Click Here</a>
   link = driver.find_element(By.LINK_TEXT, "Click Here")
   link.click()

   window_handles = driver.window_handles #2
   print(window_handles)

   for handle in window_handles:
      driver.switch_to.window(handle)   #child
      if "New Window" in driver.page_source:
         print("Testcase Passed")
         break

   time.sleep(10)
   driver.quit()
