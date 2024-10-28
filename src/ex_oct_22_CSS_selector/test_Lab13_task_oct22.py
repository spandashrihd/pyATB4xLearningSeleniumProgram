from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("macmini title and prices listing in ebay website")
@allure.description("Verify that title and price of the macmini in e bay website using xpath")
def test_item_and_price_listing_ebay():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    #Find search bar web element
    #<input type="text" class="gh-tb ui-autocomplete-input" aria-autocomplete="list" aria-expanded="false" size="50" maxlength="300" aria-label="Search for anything" placeholder="Search for anything" id="gh-ac" name="_nkw" autocapitalize="off" autocorrect="off" spellcheck="false" autocomplete="off" aria-haspopup="true" role="combobox" aria-owns="ui-id-1">
    web_element_search_bar=driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    web_element_search_bar.send_keys("macmini")

    #find search icon web element
    #<input type="submit" class="btn btn-prim gh-spr" id="gh-btn" value="Search" form="gh-f">
    web_element_search_icon=driver.find_element(By.XPATH, "//input[@value='Search']")
    web_element_search_icon.click()
    time.sleep(10)

    #find all items title web element
    #<div class="s-item__title"><span role="heading" aria-level="3"><!--F#f_0-->Shop on eBay<!--F/--></span></div>
    list_of_items=driver.find_elements(By.CSS_SELECTOR,"div[class='s-item__title']")
    list_of_prices=driver.find_elements(By.CSS_SELECTOR, "span[class='s-item__price']")
    for i in list_of_items:
        print(i.text)


    time.sleep(5)
    driver.quit()