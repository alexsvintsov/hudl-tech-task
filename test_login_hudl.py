import time
import pytest

from pages.main_page import *
from pages.hudl_login_page import *

class TestLoginHudl:
    @pytest.mark.parametrize("login_locator, partner_name",[
        (MainPage.hudl_login_locator, "Hudl"),
        (MainPage.wyscout_login_locator, "Wyscout"),
        (MainPage.volleymetrics_login_locator, "Volleymetrics"),
        (MainPage.wimu_login_locator, "WIMU"),
        (MainPage.instat_basketball_login_locator, "Instat Basketball"),
        (MainPage.instat_icehockey_login_locator, "Instat Ice Hockey"),
        (MainPage.iq_login_locator, "IQ American Football")
    ])
    def test_main_page_login_options(self, driver: webdriver, login_locator: dict, partner_name: str):
        # open main page
        main_page = MainPage(driver)
        main_page.open_main_page()

        # check that main menu is displayed
        main_menu = main_page.get_main_menu()
        assert main_menu.is_displayed(), "Main menu is not displayed"

        #check that login option is displayed
        login = main_page.get_login(login_locator)
        assert login.is_displayed(), partner_name + " login option is not displayed in main menu"

    def test_go_to_hudl_login_page(self, driver: webdriver):
        # open main page
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.hudl_login_locator)

        #check that hudl login page is displayed correctly
        hudl_login_page = HudlLoginPage(driver)
        assert hudl_login_page.driver.title == "Log In", "Unexpected page title"
        email_input = hudl_login_page.get_email_input()
        assert email_input.is_displayed()
        submit_email = hudl_login_page.get_submit_email_button()
        assert submit_email.is_displayed()

    @pytest.mark.parametrize("login_locator, partner_name",[
        (MainPage.wyscout_login_locator, "Wyscout"),
        (MainPage.volleymetrics_login_locator, "Volleymetrics"),
        (MainPage.instat_basketball_login_locator, "Instat Basketball"),
        (MainPage.instat_icehockey_login_locator, "Instat Ice Hockey"),
    ])
    def test_go_to_partner_login_page(self, driver: webdriver, login_locator: dict, partner_name: str):
        # open main page
        main_page = MainPage(driver)
        main_page.go_to_login_page(login_locator)

    def test_go_to_wimu_login_page(self, driver: webdriver):
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.wimu_login_locator)

    def test_go_to_iq_login_page(self, driver: webdriver):
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.iq_login_locator)