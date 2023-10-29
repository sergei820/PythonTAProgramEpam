# suite precondition: User is registered
# 1.
# step 1: click login button
#   expected result: login and password fields are presented
# step 2 set up login and password and click login button
#   expected result: Log out button is presented;  Welcome {username} message is presented
import pytest


@pytest.mark.usefixtures("setup")
class TestDemoBlaze:
    base_url = "https://www.demoblaze.com"

    def test_login(self):
        self.driver.get(self.base_url)
#
# 2.
# test precondition: User is logged in
# step 1: Click on Monitors category
# step 2: Click on the product with the highest price on the page
#   expected result: product's page with {product_name} and {product_price} is open
# step 3: Click on Add to cart button
# step 4: Click on Cart button
#   expected result: product is successfully added to cart; {product_name} and {product_price} are presented
