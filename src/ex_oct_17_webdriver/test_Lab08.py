from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#using Chrome browser
def test_katalon_current_url_verification():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")

    # 1.Find the element of anchor tag
    #this function find the element by locator
    # 2.we need to find the unique attribute, which can find the web element
    # <a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    # class ="btn btn-dark btn-lg" >
    # Make Appointment
    # <a/>

    make_appointment_element=driver.find_element(By.ID, "btn-make-appointment")

    # 3.Click() on it
    make_appointment_element.click()

    # 4.Verify that URL changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)
    driver.quit()
