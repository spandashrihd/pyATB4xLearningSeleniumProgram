import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Exceptions")
@allure.description("Verify Exceptions")
def test_exception_verification():
   driver = webdriver.Chrome()
   driver.get("https://app.vwo.com/")
   web_element = driver.find_element(By.ID, "this is not a ID")

   #response = {'status': 404, 'value': '{"value":{"error":"no such element",
   # "message":"no such element: Unable to locate element: {\...07FF6E343EB79]\\n\\tBaseThreadInitThunk [0x00007FFA73407374+20]\\n\\tRtlUserThreadStart [0x00007FFA749BCC91+33]\\n"}}'}

   #NoSuchElementException



   time.sleep(5)