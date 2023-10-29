import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="function")
def setup(request):
    chrome_driver_path = "driver/chromedriver-win64/chromedriver.exe"
    chrome_service = ChromeService(chrome_driver_path)
    driver = webdriver.Chrome(service=chrome_service)
    request.cls.driver = driver
    yield
    driver.quit()
