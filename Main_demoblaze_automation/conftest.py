import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser_name",
                     action="store",
                     default="chrome",
                     help="browser selection: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                  options=options)

    elif browser_name == "firefox":

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()

    else:
        raise ValueError("Please provide a valid browser name: chrome or firefox")

    driver.get("https://www.demoblaze.com")

    yield driver

    driver.quit()
