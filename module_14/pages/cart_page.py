from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CartPage:
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "#tbodyid td:nth-of-type(2)")
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR, "#tbodyid td:nth-of-type(3)")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def check_product_added_to_cart_with_correct_name_and_price(self, product_name_expected: str, product_price_expected: str):
        product_name = self.wait.until(ec.visibility_of_element_located(self.PRODUCT_NAME_IN_CART))
        assert product_name.text == product_name_expected
        product_price = self.driver.find_element(*self.PRODUCT_PRICE_IN_CART)
        assert product_price.text == product_price_expected
