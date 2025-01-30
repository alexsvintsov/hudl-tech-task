from pages.main_page import *
from pages.hudl_login_page import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestLoginToHudl:
    @allure.title("Test successful sign in")
    @allure.description("Check that it is possible to sign in to Hudl using valid credentials")
    def test_sign_in_to_hudl(self, driver: webdriver, credentials: dict):
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.hudl_login_locator, HudlLoginPage.url)

        hudl_login_page = HudlLoginPage(driver)
        with allure.step("Check that the 'email' input field is displayed"):
            email = hudl_login_page.get_email_input()
            assert email.is_displayed()

        with allure.step("Check that the 'email' input field is validated on the HTML side"):
            assert email.get_attribute("required") is not None
            assert email.get_attribute("inputmode") == "email"

        with allure.step("Enter valid email"):
            email.clear()
            email.send_keys(credentials["email"])
            submit_email = hudl_login_page.get_submit_button()

        with allure.step("Click 'Continue' to submit email and proceed to password"):
            submit_email.click()

        with allure.step("Check that the 'password' input field is displayed"):
            WebDriverWait(hudl_login_page.driver, 5).until(
                ec.visibility_of_element_located((
                    HudlLoginPage.password_locator["search_by"],
                    HudlLoginPage.password_locator["locator"],
                ))
            )

        with allure.step("Check that the 'password' input field is validated on the HTML side"):
            password = hudl_login_page.get_password_input()
            assert password.get_attribute("required") is not None

        with allure.step("Enter valid password"):
            password.clear()
            password.send_keys(credentials["password"])

        with allure.step("Click 'Continue' to submit password and proceed to home page"):
            submit_password = hudl_login_page.get_submit_button()
            submit_password.click()

        with allure.step("Check that the user if successfully logged in with valid credentials"):
            WebDriverWait(hudl_login_page.driver, 30).until(
                lambda wait_loading: HudlLoginPage.home_url in hudl_login_page.driver.current_url
            )

    @allure.title("Test invalid credentials")
    @allure.description("Check that the correct error message is displayed"
                        + " when trying to login into Hudl with invalid credentials")
    def test_invalid_hudl_credentials(self, driver: webdriver, credentials: dict):
        main_page = MainPage(driver)
        main_page.go_to_login_page(MainPage.hudl_login_locator, HudlLoginPage.url)

        hudl_login_page = HudlLoginPage(driver)
        email = hudl_login_page.get_email_input()
        with allure.step("Enter valid email"):
            email.clear()
            email.send_keys(credentials["email"])
            submit_email = hudl_login_page.get_submit_button()

        with allure.step("Click 'Continue' to submit email and proceed to password"):
            submit_email.click()

        with allure.step("Check that the 'password' input field is displayed"):
            WebDriverWait(hudl_login_page.driver, 5).until(
                ec.visibility_of_element_located((
                    HudlLoginPage.password_locator["search_by"],
                    HudlLoginPage.password_locator["locator"],
                ))
            )

        with allure.step("Enter invalid password"):
            password = hudl_login_page.get_password_input()
            password.clear()
            password.send_keys("invalid_password")

        with allure.step("Click 'Continue' to submit password"):
            submit_password = hudl_login_page.get_submit_button()
            submit_password.click()

        with allure.step("Check that the error message is displayed"):
            WebDriverWait(hudl_login_page.driver, 5).until(
                ec.visibility_of_element_located((
                    HudlLoginPage.invalid_credentials_locator["search_by"],
                    HudlLoginPage.invalid_credentials_locator["locator"]
                ))
            )
            invalid_credentials_msg = hudl_login_page.get_invalid_credentials_message()
            assert "Your email or password is incorrect. Try again." in invalid_credentials_msg.text