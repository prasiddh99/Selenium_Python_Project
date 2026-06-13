from pages.home_page import HomePage


class TestProducts:

    def test_filter_phones(self, driver):
        home = HomePage(driver)

        home.open_phones()

    def test_filter_laptops(self, driver):
        home = HomePage(driver)

        home.open_laptops()

    def test_filter_monitors(self, driver):
        home = HomePage(driver)

        home.open_monitors()

    def test_add_single_product(self, driver):
        home = HomePage(driver)

        home.add_product_to_cart("Samsung galaxy s6")
