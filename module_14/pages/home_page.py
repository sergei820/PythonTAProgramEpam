from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:
    LOGIN_BUTTON = (By.ID, "login2")
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOG_IN_BUTTON_IN_MODAL_WINDOW = (By.XPATH, "//div[@class='modal-footer']/button[text()='Log in']")
    LOGOUT_BUTTON = (By.ID, "logout2")
    WELCOME_MESSAGE = (By.ID, "nameofuser")

    MONITORS_CATEGORY = (By.XPATH, "//div[@class='list-group']/a[text()='Monitors']")
    PRICES_XPATH = "//*[contains(text(),'$')]"
    DATA_GRID_ELEMENT = (By.ID, "tbodyid")
    MONITOR_ELEMENT = (By.XPATH, "//*[contains(text(),'monitor')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def open_home_page(self):
        self.driver.get("https://www.demoblaze.com/")

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def log_in(self, username: str, password: str):
        self.wait.until(ec.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOG_IN_BUTTON_IN_MODAL_WINDOW).click()

    def check_log_out_button_is_visible(self):
        self.wait.until(ec.visibility_of_element_located(self.USERNAME_INPUT))
        assert ec.visibility_of_element_located(self.USERNAME_INPUT)

    def validate_welcome_message_text(self, username: str):
        self.wait.until(ec.visibility_of_element_located(self.WELCOME_MESSAGE))
        welcome_message = self.driver.find_element(*self.WELCOME_MESSAGE).text
        assert welcome_message == f"Welcome {username}"

    def click_category(self, category):
        # have to reload the page because of StaleElementReferenceException,
        # that can't be solved by reinitializing the webelement:
        self.driver.get("https://www.demoblaze.com/")
        category_selector = "//div[@class='list-group']/a[text()='CATEGORY']".replace('CATEGORY', category)
        category_element = self.driver.find_element(By.XPATH, category_selector)
        category_element.click()

    # step 2: Click on the product with the highest price on the page
    #   expected result: product's page with {product_name} and {product_price} is open
    def click_on_the_highest_price_product(self):
        self.wait.until(ec.visibility_of_element_located(self.MONITOR_ELEMENT))
        # gather products prices
        prices_list = [int(price_element.text.replace('$', ''))
                       for price_element in self.driver.find_elements(By.XPATH, self.PRICES_XPATH)]
        max_price = max(prices_list)

        any_price_selector = "//*[contains(text(),'$')]/preceding-sibling::*[@class='card-title']/a"
        max_price_selector = any_price_selector.replace('$', f'${max_price}')

        max_price_element = self.driver.find_element(By.XPATH, max_price_selector)
        max_price_element.click()

