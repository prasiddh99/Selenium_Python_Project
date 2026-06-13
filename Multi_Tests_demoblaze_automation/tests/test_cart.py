from pages.home_page import HomePage
from pages.cart_page import CartPage


class TestCart:

    def test_add_multiple_products(self, driver):
        home = HomePage(driver)

        products = [
            "Samsung galaxy s6",
            "Sony vaio i5"
        ]

        for product in products: home.add_product_to_cart(product)

        home.open_cart()

        cart = CartPage(driver)

        assert len(cart.get_cart_products()) == 2

    def test_delete_product(self, driver):
        home = HomePage(driver)

        home.add_product_to_cart("Samsung galaxy s6")

        home.open_cart()

        cart = CartPage(driver)

        cart.delete_product("Samsung galaxy s6")
