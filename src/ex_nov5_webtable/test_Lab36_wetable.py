import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtable():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")

    #row xpath --> //table[contains(@id, 'cust')]/tbody/tr
    row_ele = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
    row = len(row_ele)
    print(row)

    #col xpath --> //table[contains(@id, 'cust')]/tbody/tr[2]td
    col_ele = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col = len(col_ele)
    print(col)

    #xpath - //table[contains(@id,'cust')]/tbody/tr[3]/td[2]
    #first part - //table[contains(@id,'cust')]/tbody/tr[
    #second part - ]/td[
    #third part - ]
    #row-(2,7) i
    #col-(1,3) j

    first_part = "//table[contains(@id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2,row+1):
        for j in range(1, col+1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            print(dynamic_path)
            #we can find the element of dynamic path in text
            data = driver.find_element(By.XPATH,dynamic_path)
            print(data.text,end=" ")
    time.sleep(5)
    driver.quit()

