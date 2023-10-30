from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.submit-button.btn_action")

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def validate_url_after_login(self):
        actual_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"
        assert actual_url == expected_url
