from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_class import BaseClass


class PlaceOrderPage(BaseClass):
    name = (By.ID, "name")
    country = (By.ID, "country")
    city = (By.ID, "city")
    card = (By.ID, "card")
    month = (By.ID, "month")
    year = (By.ID, "year")
    purchase_btn = (By.XPATH, "//button[text()='Purchase']")
    confirmation = (By.XPATH, "//h2[text()='Thank you for your purchase!']")
    ok_button = (By.XPATH, "//button[text()='OK']")
    success_popup = (By.CLASS_NAME, "sweet-alert")

    def fill_order_details(self):
        self.wait_for_visibility(self.name).send_keys("Prasiddh")
        self.wait_for_visibility(self.country).send_keys("India")
        self.wait_for_visibility(self.city).send_keys("Rajkot")
        self.wait_for_visibility(self.card).send_keys("123456789")
        self.wait_for_visibility(self.month).send_keys("05")
        self.wait_for_visibility(self.year).send_keys("2026")

    def purchase_order(self):
        self.wait_for_clickable(self.purchase_btn).click()

    def click_ok(self):
        ok_btn = self.wait_for_clickable(self.ok_button)
        self.driver.execute_script("arguments[0].click();", ok_btn)

    def wait_until_popup_disappears(self):
        self.wait.until(EC.invisibility_of_element_located(self.success_popup))

    def verify_order_success(self):
        message = self.wait_for_visibility(self.confirmation).text
        assert (message == "Thank you for your purchase!")
