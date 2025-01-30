from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class HudlLoginPage:
    email_locator = {
        "search_by": By.ID,
        "locator": ""
    }