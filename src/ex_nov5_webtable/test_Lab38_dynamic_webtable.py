#find all the elements of dynamic table
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtable_dynamic():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")

    #get the table
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    row_table = table.find_elements(By.TAG_NAME, "tr")  #//table[@summary='Sample Table']/tbody/tr[4]/td

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for e in cols:
            print(e.text)

    time.sleep(5)
    driver.quit()

