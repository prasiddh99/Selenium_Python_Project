from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass


class LoginPage(BaseClass):
    login_menu = (By.ID, "login2")
    username = (By.ID, "loginusername")
    password = (By.ID, "loginpassword")
    login_button = (By.XPATH, "//button[text()='Log in']")

    welcome_user = (By.ID, "nameofuser")

    logout_button = (By.ID, "logout2")

    def open_login(self):
        self.wait_for_clickable(self.login_menu).click()

    def enter_username(self, user):
        self.wait_for_visibility(self.username).send_keys(user)

    def enter_password(self, pwd):
        self.wait_for_visibility(self.password).send_keys(pwd)

    def click_login(self):
        self.wait_for_clickable(self.login_button).click()

    def verify_login_success(self):
        self.wait_for_visibility(self.welcome_user)

    def logout(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

        logout_btn = self.wait_for_clickable(self.logout_button)

        self.driver.execute_script("arguments[0].click();", logout_btn)
