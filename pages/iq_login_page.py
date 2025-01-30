from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class IqLoginPage:
    driver = None
    url = "https://auth.statsbomb.com/"

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def get_title(self) -> str:
        title = self.driver.find_element(By.TAG_NAME, "h1")
        return title.text