from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.orange_page import OrangePage
from pages.shop_page import ShopPage
from utils.constants import user, password

def test_five_star(driver):
    homepage = LoginPage(driver).open_page_and_login(user, password)

    # Wait for the homepage to be loaded
    WebDriverWait(driver, 3).until(
        EC.url_to_be('https://grocerymate.masterschool.com/')
    )

    homepage.click_shop()

    # Wait for the shop page to be loaded
    WebDriverWait(driver, 3).until(
        EC.url_to_be('https://grocerymate.masterschool.com/store')
    )

    shop_page = ShopPage(driver)
    shop_page.click_age_confirm_button()

    # Wait for the orange element to be present
    orange_element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(shop_page.orange_locator)
    )

    shop_page.click_orange()

    orange_page = OrangePage(driver)

    # Wait for the five-star button to be present
    five_star_button = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(orange_page.five_star_locator)
    )

    orange_page.click_five_star_button()
    orange_page.click_send_button()

    # Wait for the orange review to be present
    orange_review = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(orange_page.review_div_locator)
    )

    # Get the review rating
    user_rating = orange_page.driver.find_element(*orange_page.review_user_rate).text

    # Assert that the user rating is 5
    assert user_rating == '(5)'

    # Delete the review
    orange_page.click_review_options()
    orange_page.click_delete_button()
    orange_page.confirm_delete_alert()