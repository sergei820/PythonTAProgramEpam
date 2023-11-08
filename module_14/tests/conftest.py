import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from module_14.pages.home_page import HomePage
from module_14.config import username, password


@pytest.fixture(scope="function")
def setup(request):
    chrome_driver_path = "driver/chromedriver-win64/chromedriver.exe"
    chrome_service = ChromeService(chrome_driver_path)
    driver = webdriver.Chrome(service=chrome_service)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="function")
def driver_fixture(request):
    chrome_driver_path = "driver/chromedriver-win64/chromedriver.exe"
    chrome_service = ChromeService(chrome_driver_path)
    driver = webdriver.Chrome(service=chrome_service)
    request.cls.driver = driver
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture(scope="function")
def login_fixture(driver_fixture):
    driver = driver_fixture
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.click_login_button()
    home_page.log_in(username, password)
    return home_page


