from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from utils.constants import user, password


def _login_and_navigate_to_shop(driver):
    # Login with user and password
    homepage = LoginPage(driver).open_page_and_login(user, password)

    # Enter the Shop Page
    return homepage.click_shop()


def _add_to_cart(driver, quantity, free_shipment):
    try:
        # Login and go to Shop Page
        shop_page = _login_and_navigate_to_shop(driver)
        shop_page.enter_age('01-01-2000')
        shop_page.click_age_confirm_button()

        # Enter the quantity for the first product of the list
        shop_page.enter_first_product_quantity(quantity)

        # Add the product to the cart
        shop_page.click_first_product_add_to_cart()

        # Click checkout button
        checkout_page = shop_page.click_checkout()

        # Wait for the shipment price
        shipment_price = checkout_page.get_shipment_price()

        if free_shipment:
            # Assert that the shipment price is 0€
            assert shipment_price.text == "0€"
        else:
            # Assert that the shipment price is not 0€
            assert shipment_price.text != "0€"

    finally:
        # Remove products from cart
        checkout_page = CheckoutPage(driver)
        checkout_page.click_remove_product()


def test_higher_than_20(driver):
    _add_to_cart(driver, 50, True)


def test_lower_than_20(driver):
    _add_to_cart(driver, 1, False)
