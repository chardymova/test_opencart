from .BasicPage import BasicPage
from locators.ProductPage import ProductPageLoc
from locators.Common import CartLoc


class ProductPage(BasicPage):
    def add_to_cart(self):
        self._click_on_element(ProductPageLoc.Actions.add_to_cart)
        return self

    def go_to_cart(self):
        self._click_on_element(CartLoc.cart_button)
        return self

    def add_to_wl(self):
        pass

    def get_product_name(self):
        text = self._get_element_text(ProductPageLoc.Text.product_name)
        return text
