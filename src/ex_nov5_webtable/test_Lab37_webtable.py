#From web table find “Helen Bennett” and which country she belongs to?
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtable_p2():
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
            data = driver.find_element(By.XPATH,dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                #to find which company she belongs to, we should use /preceding-sibling
                #country_path = f"{dynamic_path}/precedingm    -sibling::td"
                country_text = driver.find_element(By.XPATH,country_path).text
                print(f"Hellen Bennett is belongs to {country_text}")
    time.sleep(5)
    driver.quit()

