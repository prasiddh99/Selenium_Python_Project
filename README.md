# DemoBlaze Selenium Python Automation Framework

End-to-End Web Automation Framework developed using Selenium WebDriver with Python, Pytest, and Page Object Model (POM) architecture.

This project automates major user workflows of the DemoBlaze E-Commerce website including Registration, Login, Product Browsing, Cart Management, Checkout, and End-to-End Purchase Flow.

---

# Application Under Test

https://www.demoblaze.com

---

# Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- HTML Reports (pytest-html)
- WebDriver Manager
- Git & GitHub

---

# Framework Features

- Page Object Model Design Pattern
- Reusable Base Utilities
- Explicit Waits
- Pytest Fixtures
- HTML Reporting
- Automatic Screenshot Capture on Failures
- Data Driven Testing
- Modular Framework Structure
- Easy Scalability & Maintenance

---

# Total Automated Test Cases

50+ Automated Test Cases

---

# Project Structure

```bash
demoblaze_automation/
│
├── data/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── home_page.py
│   ├── cart_page.py
│   └── place_order_page.py
│
├── tests/
│   ├── test_registration.py
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_end_to_end.py
|
├── utilities/
|   ├── base_class.py
│   ├── test_data.py
│
├── screenshots/
├── reports/
│
├── conftest.py
└── pytest.ini
```

---

# Automated Test Coverage

## Registration Module
- Successful Registration
- Empty Field Validation
- Existing User Validation
- Invalid Data Validation

## Login Module
- Valid Login
- Invalid Login
- Empty Credentials
- Logout Validation

## Product Module
- Product Browsing
- Category Filtering
- Product Details Verification
- Add To Cart Validation

## Cart Module
- Add Multiple Products
- Delete Product
- Cart Validation
- Total Price Validation

## Checkout Module
- Successful Checkout
- Empty Checkout Fields
- Order Confirmation Validation

## End-to-End Flow
- Complete Purchase Workflow
- Login → Product Selection → Cart → Checkout

---

# Key Automation Scenarios

- User Registration & Login Validation
- Product Search & Category Filtering
- Add/Remove Products From Cart
- Checkout & Order Placement
- End-to-End Purchase Flow
- Screenshot Capture on Failure
- HTML Report Generation

---

# Reporting

HTML reports are generated automatically after execution.

```bash
reports/report.html
```

Screenshots are automatically captured on test failures.

```bash
screenshots/
```

---

# Installation

```bash
pip install selenium
pip install pytest
pip install pytest-html
pip install webdriver-manager
```

OR

```bash
pip install -r requirements.txt
```

---

# Run Tests

## Run All Tests

```bash
pytest
```

## Run Specific Test File

```bash
pytest tests/test_login.py
```

## Run Tests in Parallel with HTML Report

```bash
pytest tests -n auto --browser_name=chrome -v --html=reports/report.html --self-contained-html
```
---

# Clone Repository

```bash
git clone https://github.com/prasiddh99/Automation_Projects.git
```

---

# Run Framework

```bash
pytest
```

---

# Future Improvements

- Jenkins CI/CD Integration
- Allure Reporting
- Database Validation
- API + UI Hybrid Framework

---

# Author

Prasiddh Dharmnathi

GitHub:
https://github.com/prasiddh99
