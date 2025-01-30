from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class WimuLoginPage:
    url = "https://app.wimucloud.com/"

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
