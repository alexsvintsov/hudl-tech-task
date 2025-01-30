import pytest

from pages.main_page import *
from pages.hudl_login_page import *
from pages.partner_login_page import *
from pages.wimu_login_page import *
from pages.iq_login_page import *

class TestMainPage:
    @pytest.mark.parametrize("login_locator",[
        MainPage.hudl_login_locator,
        MainPage.wyscout_login_locator,
        MainPage.volleymetrics_login_locator,
        MainPage.wimu_login_locator,
        MainPage.instat_basketball_login_locator,
        MainPage.instat_icehockey_login_locator,
        MainPage.iq_login_locator
    ])
    def notest_main_page_login_options(self, driver: webdriver, login_locator: dict):
        # open main page
        main_page = MainPage(driver)
        main_page.open_main_page()

        # check that main menu is displayed
        main_menu = main_page.get_main_menu()
        assert main_menu.is_displayed(), "Main menu is not displayed"

        #check that login option is displayed
        main_menu.click()
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                login_locator["search_by"],
                login_locator["locator"]
            ))
        )

    def test_go_to_hudl_login_page(self, driver: webdriver):
        # open main page
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.hudl_login_locator, HudlLoginPage.url)

        #check that hudl login page is displayed correctly
        hudl_login_page = HudlLoginPage(driver)
        assert hudl_login_page.driver.title == "Log In", "Unexpected page title"

    @pytest.mark.parametrize("login_locator",[
        MainPage.wyscout_login_locator,
        MainPage.volleymetrics_login_locator,
        MainPage.instat_basketball_login_locator,
        MainPage.instat_icehockey_login_locator
    ])
    def test_go_to_partner_login_page(self, driver: webdriver, login_locator: dict):
        # open main page
        main_page = MainPage(driver)

        main_page.go_to_login_page(login_locator, PartnerLoginPage.url)

        partner_login_page = PartnerLoginPage(driver)
        assert partner_login_page.driver.title == "Log In", "Unexpected page title"

    def test_go_to_wimu_login_page(self, driver: webdriver):
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.wimu_login_locator, WimuLoginPage.url)

        wimu_login_page = WimuLoginPage(driver)
        assert wimu_login_page.driver.title == "WIMU PRO CLOUD", "Unexpected page title"

    def test_go_to_iq_login_page(self, driver: webdriver):
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.iq_login_locator, IqLoginPage.url)

        iq_login_page = IqLoginPage(driver)
        title = iq_login_page.get_title()
        assert title == "Welcome", "Unexpected page title"