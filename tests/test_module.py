from selenium.webdriver.common.by import By
import time
from page_objects.MainPage import MainPage
from locators.MainPage import MainPageLoc
from locators.common.Common import Search


def test_one(driver, address_param):
    driver.get(address_param)

    time.sleep(2)
    MainPage(driver).click_first_item(MainPageLoc.product, 2)


    # print(Search.input_field['css'])
    # print(MainPage.get_element_text('header h1'))
    # driver.find_element(By.CSS_SELECTOR, Search.input_field['css']).send_keys('1')
    #
    # driver.find_element(By.CSS_SELECTOR, Search.search_button['css']).click()
    time.sleep(2)
