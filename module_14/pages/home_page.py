from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    LOGIN_BUTTON = (By.ID, "login2")
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOG_IN_BUTTON_IN_MODAL_WINDOW = (By.XPATH, "//div[@class='modal-footer']/button[text()='Log in']")
    LOGOUT_BUTTON = (By.ID, "logout2")
    WELCOME_MESSAGE = (By.ID, "nameofuser")

    MONITORS_CATEGORY = (By.XPATH, "//div[@class='list-group']/a[text()='Monitors']")
    PRICES_XPATH = "//*[contains(text(),'$')]"

    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self):
        self.driver.get("https://www.demoblaze.com/")

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def log_in(self, username: str, password: str):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOG_IN_BUTTON_IN_MODAL_WINDOW).click()

    def check_log_out_button_is_visible(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        assert EC.visibility_of_element_located(self.USERNAME_INPUT)

    def validate_welcome_message_text(self, username: str):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.WELCOME_MESSAGE))
        welcome_message = self.driver.find_element(*self.WELCOME_MESSAGE).text
        assert welcome_message == f"Welcome {username}"

    def click_category(self, category):
        category_selector = "//div[@class='list-group']/a[text()='CATEGORY']".replace('CATEGORY', category)
        self.driver.find_element(By.XPATH, category_selector)





