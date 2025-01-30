from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class MainPage:
    driver = None

    main_nav_locator = {
        "search_by": By.CLASS_NAME,
        "locator": "mainnav__item__disclosure"
    }

    hudl_login_locator = {
        "search_by": By.XPATH,
        "locator": "//a[@data-qa-id='login-hudl']"
    }

    wyscout_login_locator = {
        "search_by": By.XPATH,
        "locator": "//a[@data-qa-id='login-wyscout']"
    }

    volleymetrics_login_locator = {
        "search_by": By.XPATH,
        "locator": "//a[@data-qa-id='login-volleymetrics']"
    }

    wimu_login_locator = {
        "search_by": By.XPATH,
        "locator": "//a[@data-qa-id='login-wimu']"
    }

    instat_basketball_login_locator = {
        "search_by": By.XPATH,
        "locator": "//a[@data-qa-id='login-instat-basketball']"
    }

    instat_icehockey_login_locator = {
        "search_by": By.XPATH,
        "locator": "//a[@data-qa-id='login-instat-icehockey']"
    }

    iq_login_locator = {
        "search_by": By.XPATH,
        "locator": "//a[@data-qa-id='login-iq']"
    }

    # click on every login
    # check title
    # enter credentials
    # click log in
    # check we're logged in

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def open_main_page(self) -> None:
        # disable "Allow cookies" top up
        self.driver.get("https://hudl.com/favicon.ico")
        self.driver.add_cookie({"name": "OptanonAlertBoxClosed", "value": "2025-01-30T13:40:40.078Z"})
        # open main page
        self.driver.get("https://www.hudl.com/")
        # check title
        WebDriverWait(self.driver, 10).until(
            ec.title_contains("Hudl")
        )
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((
                self.main_nav_locator["search_by"],
                self.main_nav_locator["locator"]
            ))
        )

    def get_main_menu(self) -> WebElement:
        main_nemu = self.driver.find_element(
            self.main_nav_locator["search_by"],
            self.main_nav_locator["locator"]
        )
        return main_nemu

    def navigate_to_hudl(self) -> None:
        # click menu
        # check that hudl login is displayed
        # click hudl login
        # for partners, wait for a helper block
        login = self.driver.find_element(
            self.hudl_login_locator["search_by"],
            self.hudl_login_locator["locator"]
        )
        login.click()
        WebDriverWait(self.driver, 10).until(ec.url_changes("https://identity.hudl.com/"))

    def navigate_to_wyscout(self) -> None:
        return