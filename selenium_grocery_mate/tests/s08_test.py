import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.alcohol_page import AlcoholPage
from pages.shop_page import ShopPage
from utils.constants import user, password


def test_invalid_age(driver):
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
    shop_page = ShopPage(driver)

    # Enter valid age
    shop_page.enter_age("01-01-2020")

    # Wait for value to be populated
    WebDriverWait(driver, 8).until(
        EC.text_to_be_present_in_element_value(
            shop_page.age_input_locator,
            "01-01-2020"
        )
    )

    # Click confirm age button
    shop_page.click_age_confirm_button()

    # Wait for the alcohol link to be present
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(shop_page.alcohol_locator)
    )

    # Click alcochol page
    shop_page.click_alcohol()

    # Wait for the alcohol page to be loaded
    WebDriverWait(driver, 3).until(
        EC.url_to_be('https://grocerymate.masterschool.com/store#')
    )

    # Assert no underage warning appears
    alcohol_page = AlcoholPage(driver)
    assert alcohol_page.is_underage_message_visible()
