from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.place_order_page import PlaceOrderPage

from utilities.test_data import products


def test_complete_purchase_flow(driver):
    try:

        # LOGIN
        login = LoginPage(driver)

        login.open_login()

        login.enter_username("prasiddh")

        login.enter_password("Parth@12345")

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

        raise  # raise is used to throw an exception.
        # ensures the failure is reported to Pytest
        # use it inside an except block after logging the error and taking a screenshot.
