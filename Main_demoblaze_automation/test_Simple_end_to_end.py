import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

with open('Main_demoblaze_automation/data/credentials1.json') as f:
    test_data = json.load(f)

user_credentials_list = test_data["user_credentials"]
products = test_data["products"]


@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_Simple_end_to_end(user_credentials):
    userName = user_credentials["userEmail"]
    password = user_credentials["userPassword"]

    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.demoblaze.com/")

    wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    ).send_keys(userName)

    driver.find_element(By.ID, "loginpassword").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    # Wait for login success
    wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
    print("Login Successful")

    for product in products:
        # Select Product
        wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, product))
        ).click()

        # Add To Cart
        wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))
        ).click()

        # Handle Alert
        time.sleep(2)
        alert = Alert(driver)
        print("Alert Message:", alert.text)
        alert.accept()

        print(f"{product} Added To Cart")

        # Go back to Home for next product
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.nav-link[href='index.html']"))
        ).click()

    # Go To Cart
    driver.find_element(By.ID, "cartur").click()

    # Place Order
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Place Order']")
        )
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "name"))
    ).send_keys("Prasiddh")

    driver.find_element(By.ID, "country").send_keys("India")
    driver.find_element(By.ID, "city").send_keys("Rajkot")
    driver.find_element(By.ID, "card").send_keys("123456789")
    driver.find_element(By.ID, "month").send_keys("May")
    driver.find_element(By.ID, "year").send_keys("2026")

    driver.find_element(By.XPATH, "//button[text()='Purchase']").click()

    # Verify Order Success
    success_msg = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[text()='Thank you for your purchase!']")
        )
    )
    print(success_msg.text)

    driver.find_element(By.XPATH, "//button[text()='OK']").click()

    print("Order Placed Successfully")

    time.sleep(3)
    driver.quit()
