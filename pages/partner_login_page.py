from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class PartnerLoginPage:
    url = "https://identity.hudl.com/"
    home_url = ""

    notification_box_locator = {
        "search_by": By.XPATH,
        "locator": "//div[@class='notification-box']"
    }

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

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
