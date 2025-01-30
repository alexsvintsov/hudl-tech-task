import pytest
from pages.main_page import *
from pages.hudl_login_page import *

class TestLoginToHudl:
    def test_go_to_hudl_login_page(self, driver: webdriver):
        # open main page
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.hudl_login_locator, HudlLoginPage.url)

        #check that hudl login page is displayed correctly
        hudl_login_page = HudlLoginPage(driver)
        email = hudl_login_page.get_email_input()
        assert email.is_displayed()