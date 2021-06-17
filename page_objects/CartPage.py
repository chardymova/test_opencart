from .BasicPage import BasicPage
from locators.CartPage import CartPageLoc


class CartPage(BasicPage):
    def get_last_added_product_name(self):
        text = self._get_element_text(CartPageLoc.last_added_product_name)
        return text
