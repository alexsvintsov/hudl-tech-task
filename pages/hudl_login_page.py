from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class HudlLoginPage:
    url = "https://identity.hudl.com/"

    email_locator = {
        "search_by": By.XPATH,
        "locator": "//input[contains(@id, 'username')]"
    }

    submit_email_locator = {
        "search_by": By.XPATH,
        "locator": "//button[@type='submit']"
    }

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def get_email_input(self) -> WebElement:
        email = self.driver.find_element(
            self.email_locator["search_by"],
            self.email_locator["locator"]
        )
        return email

    def get_submit_email_button(self) -> WebElement:
        submit_email = self.driver.find_element(
            self.submit_email_locator["search_by"],
            self.submit_email_locator["locator"]
        )
        return submit_email