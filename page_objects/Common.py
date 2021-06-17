from .BasicPage import BasicPage
from locators.Common import SearchLoc, CartLoc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Cart(BasicPage):
    def click_cart_button(self):
        self._click_on_element(CartLoc.cart_button)
        return self

    def click_view_cart(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, CartLoc.cart_view['css'])))
        element.click()
        return self


class Search:
    pass
