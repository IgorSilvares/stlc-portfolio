import pytest
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from utils.constants import user, password


def _login_and_navigate_to_shop(driver):
    """Login and navigate to shop page"""
    homepage = LoginPage(driver).open_page_and_login(user, password)
    return homepage.click_shop()


@pytest.mark.parametrize("quantity,expected_free_shipment", [
    pytest.param(50, True),
    pytest.param(1, False),
])
def test_shipment_pricing(driver, quantity, expected_free_shipment):
    """Test shipment pricing based on product quantity"""
    try:
        # Setup test
        shop_page = _login_and_navigate_to_shop(driver)
        shop_page.enter_age('01-01-2000')
        shop_page.click_age_confirm_button()

        # Enter quantity and add to cart
        shop_page.enter_first_product_quantity(quantity)
        shop_page.click_first_product_add_to_cart()

        # Proceed to checkout
        checkout_page = shop_page.click_checkout()
        shipment_price = checkout_page.get_shipment_price()

        # Verify shipment pricing
        if expected_free_shipment:
            assert shipment_price.text == "0€"

        else:
            assert shipment_price.text != "0€"

    finally:
        # Cleanup
        checkout_page = CheckoutPage(driver)
        checkout_page.click_remove_product()
