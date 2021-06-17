from page_objects.MainPage import MainPage
from page_objects.CartPage import CartPage
from page_objects.ProductPage import ProductPage
from page_objects.Common import Cart


def test_add_to_cart(driver, address_param):
    driver.get(address_param)
    MainPage(driver).click_item(id=1)
    name_product_page = ProductPage(driver).add_to_cart().get_product_name()
    Cart(driver).click_cart_button().click_view_cart()
    name_cart_page = CartPage(driver).get_last_added_product_name()
    assert name_product_page == name_cart_page
