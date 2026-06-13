from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass


class HomePage(BaseClass):
    add_to_cart_button = (By.LINK_TEXT, "Add to cart")

    cart_menu = (By.ID, "cartur")

    home_logo = (By.ID, "nava")

    def add_product_to_cart(self, product_name):
        product_locator = (By.LINK_TEXT, product_name)

        self.wait_for_clickable(product_locator).click()

        self.wait_for_clickable(self.add_to_cart_button).click()

        alert = self.wait_for_alert()

        print(alert.text)

        alert.accept()

        print(product_name, "added successfully")

        self.wait_for_clickable(self.home_logo).click()

    def open_cart(self):
        self.wait_for_clickable(self.cart_menu).click()
