import time
import pytest
from selenium import webdriver

from pages.main_page import MainPage

class TestLoginHudl:

    #def test_empty_email(self):

    #def test_empty_password(self):

    @pytest.mark.parametrize("parameter,value",[
        ("email", "invalid@email"),
        ("password", "invalid_password")
    ])
    def test_invalid_credentials(self, driver: webdriver, credentials: dict, parameter: str, value: str):
        # open main page
        # check selector
        # navigate to login page
        # check url
        # check title
        # check input field
        print("starting test")
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_menu = main_page.get_main_menu()
        assert main_menu.is_displayed(), "Main menu is not displayed"