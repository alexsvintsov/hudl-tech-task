import os
import json
import pytest
import allure
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture()
def driver(request) -> webdriver:
    with allure.step("Initiate browser"):
        browser_name = request.config.getoption("--browser")
        if browser_name == "chrome":
            with allure.step("Browser: Chrome"):
                driver = webdriver.Chrome()
        elif browser_name == "firefox":
            with allure.step("Browser: Firefox"):
                driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    with allure.step("Shutdown browser"):
        driver.close()
        driver.quit()

@pytest.fixture
@allure.title("Read credentials from file")
def credentials() -> dict:
    credentials_filepath = "./credentials.json"
    if not os.path.exists(credentials_filepath):
        raise FileNotFoundError(f"File not found: {credentials_filepath}")

    with open(credentials_filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Validate required keys
    if "email" not in data or "password" not in data:
        raise KeyError("Missing 'email' or 'password' key in JSON data")

    return data