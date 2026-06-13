# pages/signup_page.py
import time

from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass


class SignupPage(BaseClass):

    signup_menu = (By.ID, "signin2")
    username = (By.ID, "sign-username")
    password = (By.ID, "sign-password")
    signup_button = (By.XPATH, "//button[text()='Sign up']")
    close_button = (
        By.XPATH,"//div[@id='signInModal']//button[text()='Close']")

    def open_signup(self):
        self.wait_for_clickable(self.signup_menu).click()

    def enter_username(self, user):
        self.wait_for_visibility(self.username).send_keys(user)

    def enter_password(self, pwd):
        self.wait_for_visibility(self.password).send_keys(pwd)

    def click_signup(self):
        self.wait_for_clickable(self.signup_button).click()

    def close_signup(self):
        self.wait_for_clickable(self.close_button).click()

    def signup_user(self, user, pwd):
        self.open_signup()
        self.enter_username(user)
        self.enter_password(pwd)
        self.click_signup()

    def get_alert_text(self):
        # time.sleep(2)
        alert = self.wait_for_alert()
        text = alert.text
        alert.accept()
        return text