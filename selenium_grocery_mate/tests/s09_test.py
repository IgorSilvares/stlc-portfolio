import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.alcohol_page import AlcoholPage
from pages.shop_page import ShopPage
from utils.constants import user, password


def test_empty_age(driver):
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

    # Click confirm age button without a age
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
