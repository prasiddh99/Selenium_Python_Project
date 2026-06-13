import pytest
from pages.login_page import LoginPage


@pytest.mark.login
class TestLogin:

    def test_valid_login(self, driver):
        login = LoginPage(driver)

        login.open_login()

        login.enter_username("prasiddh")

        login.enter_password("Parth@12345")

        login.click_login()

        login.verify_login_success()

    @pytest.mark.parametrize(
        "username,password",
        [
            ("wronguser", "Parth@12345"),
            ("prasiddh", "wrongpass"),
            ("", "Parth@12345"),
            ("prasiddh", ""),
            ("", "")
        ])
    def test_invalid_login(
            self,
            driver,
            username,
            password):
        login = LoginPage(driver)

        login.open_login()

        login.enter_username(username)

        login.enter_password(password)

        login.click_login()

        alert_text = login.get_alert_text()

        assert alert_text != ""
