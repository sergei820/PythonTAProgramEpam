# For this site https://www.saucedemo.com/
#  using Selenium Webdriver methods need to create some script with these steps:
#  1. open site (https://www.saucedemo.com/)
#  2. paste correct name into Username field (info below)
#  3. paste correct password into Password field (info below also)
#  4. click to Login button
#  5. get current URL
#  6. check that current URL and expected URL (https://www.saucedemo.com/inventory.html, for example) are the same
#
#
#  IMPORTANT OBJECTIVE FOR THIS TASK:
#  need to use at least 2 different methods for locators search
#  (for example, using DOM and XPath: By.ID for username field and By.XPATH for password field)
#
#
#  CREDENTIALS
#  You can find them on the main page. For example these ones:
#  standard_user
#  secret_sauce
#
#
#  ### Dont forget about Selenium and Webdriver
#
#
#  To install selenium use this command - pip install selenium.
#  For local run need to download and install Selenium WebDriver
#  (for Google Chrome, for example, you can use this link - https://chromedriver.chromium.org/downloads).
#  Major versions of your browser and your webdriver should be the same.
#  More info - https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver
from selenium.webdriver.common.by import By
from selenium import webdriver


class Locators:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.submit-button.btn_action")


class LoginPage:
    pass


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

