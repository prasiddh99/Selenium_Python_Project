import pytest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.place_order_page import PlaceOrderPage
from utilities.json_reader import get_test_data

# pytest tests/test_data_driven.py --browser_name=firefox -v

test_data = get_test_data()
user_credentials_list = test_data["user_credentials"]
products = test_data["products"]

@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_complete_purchase_flow(driver, user_credentials):
    try:

        userName = user_credentials["userEmail"]
        password = user_credentials["userPassword"]

        # LOGIN
        login = LoginPage(driver)

        login.open_login()

        login.enter_username(userName)

        login.enter_password(password)

        login.click_login()

        login.verify_login_success()

        print("Login successful")

        # HOME PAGE
        home = HomePage(driver)

        # MULTIPLE PRODUCTS
        for product in products:
            home.add_product_to_cart(product)

        print("All products added")

        # OPEN CART
        home.open_cart()

        # CART PAGE
        cart = CartPage(driver)

        cart.click_place_order()

        # PLACE ORDER PAGE
        order = PlaceOrderPage(driver)

        order.fill_order_details()

        order.purchase_order()

        order.verify_order_success()

        order.click_ok()

        print("OK button clicked")

        order.wait_until_popup_disappears()

        print("Order placed successfully")

        # LOGOUT
        login.logout()

        print("Logout successful")

    except Exception as e:

        print("Test Failed:", e)

        login.take_screenshot("test_failure")

        raise
