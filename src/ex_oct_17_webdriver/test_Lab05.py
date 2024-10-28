from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_chrome_options():

    chrome_option=Options()
    chrome_option.add_argument("--incognito")   #chrome incognito mode
    #chrome_option.add_argument("--start-maximized")  #for maximizing session window
    #chrome_option.add_argument("--window-size")  #for making 900x600 windows size
    #chrome_option.add_argument("--headless") #no UI will be shown
    driver=webdriver.Chrome(chrome_option)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    #stop the python interpreter for 10 second
    time.sleep(10)
