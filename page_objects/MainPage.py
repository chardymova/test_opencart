from .BasicPage import BasicPage
from locators.MainPage import MainPageLoc
class MainPage(BasicPage):
    def click_first_item(self, selector, id=1):
        self._click_on_element(selector, id)
    # def get_featured_product_name(self, number):
    #     index = number - 1
    #     return self._get_element_text(MainPageLoc.featured.names, index=index)