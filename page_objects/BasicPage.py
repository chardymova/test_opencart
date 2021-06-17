from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasicPage:
    def __init__(self, driver):
        self.driver = driver

    def __elements(self, selector: dict, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)

    def _click_on_element(self, selector, index=1):
        index -= 1
        return self.__elements(selector=selector)[index].click()

    def _get_element_text(self, selector, index=1):
        index -= 1
        return self.__elements(selector=selector)[index].text

    def _get_element_len(self, selector):
        return len(self.__elements(selector))