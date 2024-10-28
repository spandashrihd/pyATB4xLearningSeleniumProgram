import time
import allure
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

@allure.title("Exceptions handling")
@allure.description("Verify Exceptions handles")
def test_exception_handle_verification():
   driver = webdriver.Chrome()
   driver.get("https://app.vwo.com/")

   #handling exception
   try:
       web_element = driver.find_element(By.ID, "this ID doesn't exist")

   # NoSuchElementException
   except NoSuchElementException as nse:
       print(nse.msg)

   time.sleep(5)