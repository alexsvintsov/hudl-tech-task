from selenium import webdriver

class WimuLoginPage:
    url = "https://app.wimucloud.com/"

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
