from selenium import webdriver
from module_13.pages.login_page import LoginPage


def test_login():
    chrome_driver_path = "../driver/chromedriver-win64/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    driver.quit()

