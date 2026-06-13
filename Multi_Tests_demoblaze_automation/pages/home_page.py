import time

from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass


class HomePage(BaseClass):
    add_to_cart_button = (By.LINK_TEXT, "Add to cart")
    cart_menu = (By.ID, "cartur")
    home_logo = (By.ID, "nava")
    phones_category = (By.LINK_TEXT, "Phones")
    laptops_category = (By.LINK_TEXT, "Laptops")
    monitors_category = (By.LINK_TEXT, "Monitors")

    def add_product_to_cart(self, product_name):
        self.driver.refresh()

        product_locator = (By.LINK_TEXT, product_name)

        self.wait_for_clickable(product_locator).click()

        self.wait_for_clickable(self.add_to_cart_button).click()

        alert = self.wait_for_alert()

        print(alert.text)

        alert.accept()
        time.sleep(2)
        print(product_name, "added successfully")
        self.wait_for_clickable(self.home_logo).click()
        time.sleep(2)

    def open_cart(self):
        self.wait_for_clickable(self.cart_menu).click()

    def open_phones(self):
        self.wait_for_clickable(self.phones_category).click()

    def open_laptops(self):
        self.wait_for_clickable(self.laptops_category).click()

    def open_monitors(self):
        self.wait_for_clickable(self.monitors_category).click()
