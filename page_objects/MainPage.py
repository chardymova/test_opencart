from .BasicPage import BasicPage
from locators.MainPage import MainPageLoc


class MainPage(BasicPage):
    def click_item(self, selector=MainPageLoc.products, id=1):
        self._click_on_element(selector, id)
        return self

    def get_len(self, selector):
        return self._get_element_len(selector)