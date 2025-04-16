import pytest
from pages.login_page import LoginPage
from utils.constants import user, password


def _login_and_navigate_to_shop(driver):
    """Login and navigate to shop page"""
    homepage = LoginPage(driver).open_page_and_login(user, password)
    return homepage.click_shop()


@pytest.mark.parametrize("initial_qty,add_clicks,remove_clicks,expected_shipment", [
    # Test 1: Add 1 item + 40 clicks = 41 items (free shipping)
    (1, 40, 0, "0€"),
    # Test 2: Add 30 items - 29 clicks = 1 item (paid shipping)
    (30, 0, 29, "5€"),
])
def test_shipping_threshold_with_quantity_changes(
        driver, initial_qty, add_clicks, remove_clicks, expected_shipment
):
    """
    Test shipping price changes when:
    - Adding multiple items to reach free shipping threshold
    - Removing items to fall below threshold
    """
    checkout_page = None
    try:
        # Setup test
        shop_page = _login_and_navigate_to_shop(driver)
        shop_page.enter_age('01-01-2000')
        shop_page.click_age_confirm_button()

        # Enter quantity and add to cart
        shop_page.enter_first_product_quantity(initial_qty)
        shop_page.click_first_product_add_to_cart()

        # Proceed to checkout
        checkout_page = shop_page.click_checkout()

        # Click add button specified times
        for _ in range(add_clicks):
            checkout_page.click_plus_product_button()

        # Click remove button specified times
        for _ in range(remove_clicks):
            checkout_page.click_minus_product_button()

        # 3. Verify expected shipping price
        assert checkout_page.get_shipment_price().text == expected_shipment

    finally:
        # Cleanup
        if checkout_page:
            checkout_page.click_remove_all_button()
