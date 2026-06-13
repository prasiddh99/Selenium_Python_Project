from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time


class BaseClass:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_alert(self):
        return self.wait.until(EC.alert_is_present())

    def take_screenshot(self, file_name):
        folder = "screenshots"

        if not os.path.exists(folder):
            os.makedirs(folder)

        timestamp = time.strftime("%Y%m%d-%H%M%S")

        path = f"{folder}/{file_name}_{timestamp}.png"

        self.driver.save_screenshot(path)

        print(f"Screenshot saved: {path}")
