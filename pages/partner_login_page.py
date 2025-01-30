from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class PartnerLoginPage:
    url = "https://identity.hudl.com/"

    helper_locator = {
        "search_by": By.ID,
        "locator": ""
    }

    email_locator = {
        "search_by": By.ID,
        "locator": ""
    }

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
