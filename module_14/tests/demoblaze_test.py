import pytest

from module_14.pages.home_page import HomePage
from module_14.pages.product_page import ProductPage


@pytest.mark.usefixtures("setup")
class TestDemoBlaze:
    base_url = "https://www.demoblaze.com"

    def test_login_test(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.click_login_button()
        home_page.log_in("snowfallslow@gmail.com", "1qa2ws3ed")
        home_page.check_log_out_button_is_visible()
        home_page.validate_welcome_message_text("snowfallslow@gmail.com")

    def test_add_to_cart_test(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.click_login_button()
        home_page.log_in("snowfallslow@gmail.com", "1qa2ws3ed")
        home_page.click_category('Monitors')
        home_page.click_on_the_highest_price_product()
        product_page = ProductPage(self.driver)
        product_page.check_the_products_page_opened("Apple monitor 24", "$400")
        product_page.click_on_add_to_cart_button()
        product_page.click_on_cart_button()
        cart_page = CartPage(self.driver)
        #   expected result: product is successfully added to cart; {product_name} and {product_price} are presented
