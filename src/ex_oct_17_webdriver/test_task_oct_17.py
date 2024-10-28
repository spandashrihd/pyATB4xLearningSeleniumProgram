from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_task_katalon_current_url_verification():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")

    # 1.Find the element of anchor tag
    # 2.We need to find the unique attribute, which can find the web element
        # <a
        # id="btn-make-appointment" 
        # href="./profile.php#login" 
        # class="btn btn-dark btn-lg">
        # Make Appointment
        # </a>
    make_appointment_element=driver.find_element(By.ID, "btn-make-appointment")

    # 3.click on it
    make_appointment_element.click()

    # 4.Verify the URL
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)

    #find username web element
    # <input type="text" class="form-control" id="txt-username" name="username" placeholder="Username" value="" autocomplete="off">
    username=driver.find_element(By.NAME, "username")
    username.send_keys("John Doe")

    #find password web element
    # < input type = "password" class ="form-control" id="txt-password" name="password" placeholder="Password" value="" autocomplete="off" >

    password= driver.find_element(By.NAME, "password")
    password.send_keys("ThisIsNotAPassword")

    #find Login button web element
    #<button id="btn-login" type="submit" class="btn btn-default">Login</button>
    login=driver.find_element(By.ID,"btn-login")
    login.click()

    time.sleep(10)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    driver.quit()

