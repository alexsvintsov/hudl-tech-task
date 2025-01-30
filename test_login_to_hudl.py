from pages.main_page import *
from pages.hudl_login_page import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestLoginToHudl:
    def test_sign_in_to_hudl(self, driver: webdriver, credentials: dict):
        # open main page
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.hudl_login_locator, HudlLoginPage.url)

        #check that hudl login page is displayed correctly
        hudl_login_page = HudlLoginPage(driver)
        email = hudl_login_page.get_email_input()
        assert email.is_displayed()
        # check that email input is validated on html side
        assert email.get_attribute("required") is not None
        assert email.get_attribute("autocomplete") == "email"
        # enter email
        email.clear()
        email.send_keys(credentials["email"])
        submit_email = hudl_login_page.get_submit_button()
        # submit email
        submit_email.click()
        WebDriverWait(hudl_login_page.driver, 5).until(
            ec.visibility_of_element_located((
                HudlLoginPage.password_locator["search_by"],
                HudlLoginPage.password_locator["locator"],
            ))
        )
        # enter password
        password = hudl_login_page.get_password_input()
        assert password.get_attribute("required") is not None
        password.clear()
        password.send_keys(credentials["password"])
        # submit password
        submit_password = hudl_login_page.get_submit_button()
        submit_password.click()
        # check that we're successfully logged in
        WebDriverWait(hudl_login_page.driver, 30).until(
            lambda wait_loading: HudlLoginPage.home_url in hudl_login_page.driver.current_url
        )

    def test_invalid_hudl_credentials(self, driver: webdriver, credentials: dict):
        # open main page
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.hudl_login_locator, HudlLoginPage.url)

        #check that hudl login page is displayed correctly
        hudl_login_page = HudlLoginPage(driver)
        email = hudl_login_page.get_email_input()
        # enter email
        email.clear()
        email.send_keys(credentials["email"])
        submit_email = hudl_login_page.get_submit_button()
        # submit email
        submit_email.click()
        WebDriverWait(hudl_login_page.driver, 5).until(
            ec.visibility_of_element_located((
                HudlLoginPage.password_locator["search_by"],
                HudlLoginPage.password_locator["locator"],
            ))
        )
        # enter password
        password = hudl_login_page.get_password_input()
        password.clear()
        password.send_keys("invalid_password")
        # submit password
        submit_password = hudl_login_page.get_submit_button()
        submit_password.click()
        # check that error message is displayed
        WebDriverWait(hudl_login_page.driver, 5).until(
            ec.visibility_of_element_located((
                HudlLoginPage.invalid_credentials_locator["search_by"],
                HudlLoginPage.invalid_credentials_locator["locator"]
            ))
        )
        invalid_credentials_msg = hudl_login_page.get_invalid_credentials_message()
        assert "Your email or password is incorrect. Try again." in invalid_credentials_msg.text