import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utils.constants import user, password


def test_higher_than_20(driver):
    try:
        # Open the login page and log in
        homepage = LoginPage(driver).open_page_and_login(user, password)

        # Wait for the homepage to be loaded
        WebDriverWait(driver, 3).until(
            EC.url_to_be('https://grocerymate.masterschool.com/')
        )

        # Click the shop button
        homepage.click_shop()

        # Wait for the shop page to be loaded
        WebDriverWait(driver, 3).until(
            EC.url_to_be('https://grocerymate.masterschool.com/store')
        )

        # Click the age confirm button
        shop_page = ShopPage(driver)
        shop_page.click_age_confirm_button()

        # 4. Wait for celery input to be present and interactable
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(shop_page.celery_quantity_locator)
        )
        # Enter Celery quantity
        shop_page.enter_celery_quantity(30)

        # Wait to be populated
        WebDriverWait(driver, 3).until(
            EC.text_to_be_present_in_element_value(
                shop_page.celery_quantity_locator,
                "30"
            )
        )

        # Get the actual button element before scrolling
        add_to_cart_btn = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(shop_page.celery_add_to_cart_button)
        )

        # Scroll the actual element into view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_btn)

        # Click add to cart
        shop_page.click_celery_add_to_cart_button()

        # Click checkout button
        shop_page.click_checkout()
        checkout_page = CheckoutPage(driver)

        # Wait for the shipment price
        shipment_price = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(checkout_page.shipment_price_locator)
        )

        # Assert that the shipment price is 0€
        assert shipment_price.text == "0€"

    finally:
        checkout_page = CheckoutPage(driver)
        checkout_page.click_remove_product()
