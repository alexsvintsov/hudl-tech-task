from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class MainPage:
    driver = None

    main_nav_locator = {
        "search_by": By.CSS_SELECTOR,
        "locator": "[data-qa-id='login-select']"
    }

    hudl_login_locator = {
        "search_by": By.CSS_SELECTOR,
        "locator": "[data-qa-id='login-hudl']"
    }

    wyscout_login_locator = {
        "search_by": By.CSS_SELECTOR,
        "locator": "[data-qa-id='login-wyscout']"
    }

    volleymetrics_login_locator = {
        "search_by": By.CSS_SELECTOR,
        "locator": "[data-qa-id='login-volleymetrics']"
    }

    wimu_login_locator = {
        "search_by": By.CSS_SELECTOR,
        "locator": "[data-qa-id='login-wimu']"
    }

    instat_basketball_login_locator = {
        "search_by": By.CSS_SELECTOR,
        "locator": "[data-qa-id='login-instat-basketball']"
    }

    instat_icehockey_login_locator = {
        "search_by": By.CSS_SELECTOR,
        "locator": "[data-qa-id='login-instat-icehockey']"
    }

    iq_login_locator = {
        "search_by": By.CSS_SELECTOR,
        "locator": "[data-qa-id='login-iq']"
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

    def get_main_menu(self) -> WebElement:
        main_nemu = self.driver.find_element(
            self.main_nav_locator["search_by"],
            self.main_nav_locator["locator"]
        )
        return main_nemu

    def get_login(self, locator) -> WebElement:
        login = self.driver.find_element(
            locator["search_by"],
            locator["locator"]
        )
        return login

    def go_to_login_page(self, locator: dict, url: str) -> None:
        # open main page
        self.open_main_page()
        # open menu
        main_menu = self.get_main_menu()
        main_menu.click()
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((
                locator["search_by"],
                locator["locator"]
            ))
        )
        # go to login page
        login = self.get_login(locator)
        login.click()
        WebDriverWait(self.driver, 30).until(
            lambda wait_loading: url in self.driver.current_url
        )
