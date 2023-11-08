import pytest

from module_14.pages.home_page import HomePage
from module_14.pages.product_page import ProductPage
from module_14.pages.cart_page import CartPage
from module_14.config import username, password


class TestDemoBlaze:

    @pytest.mark.usefixtures("setup")
    def test_login(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.click_login_button()
        home_page.log_in(username, password)
        home_page.check_log_out_button_is_visible()
        home_page.validate_welcome_message_text("snowfallslow@gmail.com")

    def test_add_to_cart(self, driver_fixture, login_fixture):
        home_page = login_fixture
        home_page.click_category('Monitors')
        home_page.click_on_the_highest_price_product()
        product_page = ProductPage(self.driver)
        product_page.check_the_products_page_opened("Apple monitor 24", "$400")
        product_page.click_on_add_to_cart_button()
        product_page.click_on_cart_button()
        cart_page = CartPage(self.driver)
        cart_page.check_product_added_to_cart_with_correct_name_and_price("Apple monitor 24", "400")
