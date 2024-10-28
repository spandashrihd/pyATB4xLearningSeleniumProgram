from selenium import webdriver

def test_current_url_verification():
    driver=webdriver.Chrome()  #using chrome browser
    #driver=webdriver.Edge() #using MS Edge
    #driver=webdriver.Firefox() #using Firefox browser
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    driver.quit()