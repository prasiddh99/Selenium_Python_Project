from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass


class CartPage(BaseClass):
    place_order_btn = (By.XPATH, "//button[text()='Place Order']")

    def click_place_order(self):
        self.wait_for_clickable(self.place_order_btn).click()
