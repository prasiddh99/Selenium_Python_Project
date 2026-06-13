import pytest
from pages.signup_page import SignupPage


@pytest.mark.registration
class TestRegistration:

    def test_successful_registration(self, driver):
        signup = SignupPage(driver)

        import time

        username = f"user{int(time.time())}"  # Generate random usernames every run.
        # DemoBlaze does NOT allow duplicate usernames.
        # if username was already registered once before, the next run fails with:
        signup.signup_user(username, "Password@123")

        alert_text = signup.get_alert_text()

        assert "Sign up successful" in alert_text

    @pytest.mark.parametrize(
        "username,password",
        [
            ("", "Password@123"),
            ("Pparth99", ""),
            ("", "")
        ]
    )
    def test_empty_registration_fields(self, driver, username, password):
        signup = SignupPage(driver)

        signup.signup_user(username, password)

        alert_text = signup.get_alert_text()

        assert "please fill out username and password" in alert_text.lower()
