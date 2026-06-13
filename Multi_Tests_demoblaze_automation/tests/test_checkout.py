from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.place_order_page import PlaceOrderPage


class TestCheckout:

    def test_successful_checkout(self, driver):
        home = HomePage(driver)

        home.add_product_to_cart("Samsung galaxy s6")

        home.open_cart()

        cart = CartPage(driver)

        cart.click_place_order()

        order = PlaceOrderPage(driver)

        order.fill_order_details()

        order.purchase_order()

        order.verify_order_success()

    def test_checkout_empty_name(self, driver):
        home = HomePage(driver)

        home.add_product_to_cart("Samsung galaxy s6")

        home.open_cart()

        cart = CartPage(driver)

        cart.click_place_order()

        order = PlaceOrderPage(driver)

        order.purchase_order()
