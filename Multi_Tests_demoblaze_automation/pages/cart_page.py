import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass


class CartPage(BaseClass):
    place_order_btn = (By.XPATH, "//button[text()='Place Order']")
    # cart_products = (By.XPATH, "//tr[@class='success']")
    cart_products = (By.XPATH, "//tbody[@id='tbodyid']/tr")

    total_amount = (By.ID, "totalp")

    def click_place_order(self):
        self.wait_for_clickable(self.place_order_btn).click()

    # def get_cart_products(self):
    #     time.sleep(2)
    #     return self.driver.find_elements(*self.cart_products)

    def get_cart_products(self):
        time.sleep(3)
        self.wait_for_presence(self.cart_products)
        return self.driver.find_elements(*self.cart_products)

    def get_total_amount(self):
        return self.wait_for_visibility(self.total_amount).text

    def delete_product(self, product_name):
        delete_btn = (
            By.XPATH, f"//td[text()='{product_name}']/following-sibling::td/a")

        self.wait_for_clickable(delete_btn).click()
