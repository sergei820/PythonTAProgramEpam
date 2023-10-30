from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage:
    # PRODUCT_NAME = (By.CSS_SELECTOR, "#tbodyid .name")
    PRODUCT_NAME = (By.XPATH, "//div[@id='tbodyid']/h2[@class='name']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#tbodyid .price-container")
    ADD_TO_CART = (By.XPATH, "//div[@id='tbodyid']//a[contains(text(),'Add to cart')]")
    CART_BUTTON = (By.XPATH, "//div[@class='navbar-collapse']//li/a[@id='cartur']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def check_the_products_page_opened(self, product_name_expected: str, product_price_expected: str):
        self.wait.until(ec.visibility_of_element_located(self.PRODUCT_NAME))
        product_name_actual = self.driver.find_element(*self.PRODUCT_NAME).text
        assert product_name_actual == product_name_expected
        product_price_actual = self.driver.find_element(*self.PRODUCT_PRICE).text
        assert product_price_expected in product_price_actual

    def click_on_add_to_cart_button(self):
        self.driver.find_element(*self.ADD_TO_CART).click()
        alert = self.wait.until(ec.alert_is_present())
        alert.accept()
        self.driver.refresh()

    def click_on_cart_button(self):
        self.wait.until(ec.visibility_of_element_located(self.CART_BUTTON))
        self.driver.find_element(*self.CART_BUTTON).click()






