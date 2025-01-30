import pytest

from pages.main_page import *
from pages.hudl_login_page import *
from pages.partner_login_page import *
from pages.wimu_login_page import *
from pages.iq_login_page import *

class TestMainPage:
    @allure.title("Test login options")
    @allure.description("Check that login pages of all partners are presented on the main page")
    @pytest.mark.parametrize("login_locator",[
        MainPage.hudl_login_locator,
        MainPage.wyscout_login_locator,
        MainPage.volleymetrics_login_locator,
        MainPage.wimu_login_locator,
        MainPage.instat_basketball_login_locator,
        MainPage.instat_icehockey_login_locator,
        MainPage.iq_login_locator
    ])
    def test_main_page_login_options(self, driver: webdriver, login_locator: dict):
        main_page = MainPage(driver)
        main_page.open_main_page()

        with allure.step("Check that Login menu is displayed"):
            login_menu = main_page.get_login_menu()
            assert login_menu.is_displayed(), "Login menu is not displayed"

        with allure.step("Check that the login option is displayed"):
            login_menu.click()
            WebDriverWait(driver, 5).until(
                ec.visibility_of_element_located((
                    login_locator["search_by"],
                    login_locator["locator"]
                ))
            )

    @allure.title("Test redirect to Hudl login page")
    @allure.description("Check that Hudl login button from Login menu works and leads to Hudl login page")
    def test_go_to_hudl_login_page(self, driver: webdriver):
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.hudl_login_locator, HudlLoginPage.url)

        with allure.step("Check that Hudl login page was loaded"):
            hudl_login_page = HudlLoginPage(driver)
            assert hudl_login_page.driver.title == "Log In", "Unexpected page title"

    @allure.title("Test redirect to a partner login page")
    @allure.description("Check that some partners' login buttons from Login menu work and lead to their login page")
    @pytest.mark.parametrize("login_locator",[
        MainPage.wyscout_login_locator,
        MainPage.volleymetrics_login_locator,
        MainPage.instat_basketball_login_locator,
        MainPage.instat_icehockey_login_locator
    ])
    def test_go_to_partner_login_page(self, driver: webdriver, login_locator: dict):
        main_page = MainPage(driver)
        main_page.go_to_login_page(login_locator, PartnerLoginPage.url)

        with allure.step("Check that partner's login page was loaded"):
            partner_login_page = PartnerLoginPage(driver)
            assert partner_login_page.driver.title == "Log In", "Unexpected page title"

    @allure.title("Test redirect to a WIMU login page")
    @allure.description("Check that WIMU login button from Login menu works and leads to WIMU login page")
    def test_go_to_wimu_login_page(self, driver: webdriver):
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.wimu_login_locator, WimuLoginPage.url)

        with allure.step("Check that WIMU login page was loaded"):
            wimu_login_page = WimuLoginPage(driver)
            assert wimu_login_page.driver.title == "WIMU PRO CLOUD", "Unexpected page title"

    @allure.title("Test redirect to a IQ login page")
    @allure.description("Check that IQ login button from Login menu works and leads to IQ login page")
    def test_go_to_iq_login_page(self, driver: webdriver):
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.iq_login_locator, IqLoginPage.url)

        with allure.step("Check that IQ login page was loaded"):
            iq_login_page = IqLoginPage(driver)
            title = iq_login_page.get_title()
            assert title == "Welcome", "Unexpected page title"