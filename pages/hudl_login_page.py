from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class HudlLoginPage:
    url = "https://identity.hudl.com/"
    home_url = "https://www.hudl.com/home"

    email_locator = {
        "search_by": By.ID,
        "locator": "username"
    }

    password_locator = {
        "search_by": By.ID,
        "locator": "password"
    }

    submit_button_locator = {
        "search_by": By.XPATH,
        "locator": "//button[@type='submit']"
    }

    invalid_credentials_locator = {
        "search_by": By.ID,
        "locator": "error-element-password"
    }

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def get_email_input(self) -> WebElement:
        email = self.driver.find_element(
            self.email_locator["search_by"],
            self.email_locator["locator"]
        )
        return email

    def get_password_input(self) -> WebElement:
        password = self.driver.find_element(
            self.password_locator["search_by"],
            self.password_locator["locator"]
        )
        return password

    def get_submit_button(self) -> WebElement:
        submit_email = self.driver.find_element(
            self.submit_button_locator["search_by"],
            self.submit_button_locator["locator"]
        )
        return submit_email

    def get_invalid_credentials_message(self) -> WebElement:
        invalid_credentials_msg = self.driver.find_element(
            self.invalid_credentials_locator["search_by"],
            self.invalid_credentials_locator["locator"]
        )
        return invalid_credentials_msg