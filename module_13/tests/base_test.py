from selenium import webdriver


class BaseTest:
    @classmethod
    def setup(cls):
        chrome_driver_path = "driver/chromedriver-win64/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    @classmethod
    def teardown(cls):
        cls.driver.quit()

