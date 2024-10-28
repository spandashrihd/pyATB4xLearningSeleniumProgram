import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("SVG")
@allure.description("Verify SVG")
def test_svg_verification():
   driver = webdriver.Chrome()
   driver.get("https://www.flipkart.com/")

   #<input class="Pke_EE" type="text" title="Search for Products, Brands and More" name="q" autocomplete="off" placeholder="Search for Products, Brands and More" value="">
   search_box = driver.find_element(By.NAME, "q")
   search_box.send_keys("macmini")


   #//*[local-name()="svg"] or //*[name()="svg"]
   list_of_svg_elements = driver.find_elements(By.XPATH, "//*[name()='svg']")
   list_of_svg_elements[0].click()

   time.sleep(5)

