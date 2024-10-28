import time
import allure
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@allure.title("Handling Timeout Exceptions")
@allure.description("Verify timeout Exceptions handles")
def test_handle_timeout_exception_verification():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    try:
        #submit element, doesn't exist, it will wait max 10 sec then throw exception
        WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable((By.ID, "submit")))
        print("End of the program")
    except TimeoutException as te:
        print(te.msg)
        print("Timeout Exception occured!, 10 sec passed")
    finally:
        driver.quit()
