import time
import allure
from selenium  import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@allure.title("Example combined Actions, windows and JS executor")
@allure.description("Verify Actions, windows and JS executor")
def test_verify_action_windows_js():
    # Chrome options --> --incoginito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/test...")
    driver.maximize_window()


    main_window_handles = driver.current_window_handle #1
    lst = driver.find_element(By.CSS_SELECTOR, "data-qa='yedexafobi']")
    #control = 0
    #version = 1

    variation = lst[1]
    print(main_window_handles)

    for handle in main_window_handles:
        driver.switch_to.window(handle)  # child
        if "New Window" in driver.page_source:
            print("Testcase Passed")
            break

    time.sleep(10)
    driver.quit()
