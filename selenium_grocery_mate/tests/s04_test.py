from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.orange_page import OrangePage
from pages.shop_page import ShopPage
from utils.constants import user, password, feedback_500char

def test_500_feedback(driver):
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

    # Wait for the orange element to be present
    orange_element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(shop_page.orange_locator)
    )

    # Click the orange element
    shop_page.click_orange()
    orange_page = OrangePage(driver)

    # Wait for the feedback input to be present
    WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(orange_page.review_text_locator)
    )

    # Enter 500 char review text
    orange_page.enter_review_text(feedback_500char)

    # Assert that the error message is present
    assert WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(orange_page.review_error_message)
    )