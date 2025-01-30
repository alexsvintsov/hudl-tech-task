import os
import json
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture()
def driver(request) -> webdriver:
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver

    driver.close()
    driver.quit()

@pytest.fixture
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