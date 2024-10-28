import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@allure.title("Select")
@allure.description("Verify Select")
def test_select_verification():
   driver = webdriver.Chrome()
   driver.get("https://the-internet.herokuapp.com/dropdown")

   #ID = "dropdown"
   select_html_tag = driver.find_element(By.ID, "dropdown")
   select_options = Select(select_html_tag)

   select_options.select_by_visible_text("Option 2")

   #usually index 0: select an option, 1: option 1, 2: option2
   #select_options.select_by_index(1)

   time.sleep(5)

