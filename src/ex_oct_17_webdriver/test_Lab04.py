from selenium import webdriver

def test_open_vwo_loin():
    driver=webdriver.Chrome()  #it will create the Session -1acc1dc25946622cd0d0970cebbd76b8
    driver.get("https://app.vwo.com")   #navigate to URL
    page_source_data= driver.page_source
    print(page_source_data)
    print(driver.session_id)

