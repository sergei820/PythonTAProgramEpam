import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    chrome_driver_path = "driver/chromedriver-win64/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    request.cls.driver = driver
    yield
    driver.quit()
