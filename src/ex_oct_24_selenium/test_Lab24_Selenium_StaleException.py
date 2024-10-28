import time
import allure
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

@allure.title("Stale Exceptions")
@allure.description("Verify stale Exceptions")
def test_stale_exception_verification():
   driver = webdriver.Chrome()
   driver.get("https://www.google.com/")

   text_area = driver.find_element(By.NAME,"q")

   driver.refresh()
   text_area.send_keys("The Testing Academy")
   #response = {'status': 404, 'value': '{"value":{"error":"stale element reference","message":"stale element reference: stale elemen...07FF6B5DBEB79]\\n\\tBaseThreadInitThunk [0x00007FFD85907374+20]\\n\\tRtlUserThreadStart [0x00007FFD85D7CC91+33]\\n"}}'}


   time.sleep(5)