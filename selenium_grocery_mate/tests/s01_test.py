import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.orange_page import OrangePage
from pages.shop_page import ShopPage
from utils.constants import user, password

def test_five_star(driver):
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

        # Wait for the search input to be present
        search_input = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(shop_page.search_input_locator)
        )

        # Search the orange item
        shop_page.enter_search("oranges")

        # Wait for the orange item to be present
        orange_item = WebDriverWait(driver, timeout=3).until(
            EC.presence_of_element_located(shop_page.searched_item_locator)
        )
        # Click the orange item
        shop_page.click_searched_item()

        # Wait fot the orange page to be loaded
        WebDriverWait(driver, timeout=3).until(
            EC.url_to_be("https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f")
        )
        orange_page = OrangePage(driver)

        # Wait for the five-star button to be present
        five_star_button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(orange_page.five_star_locator)
        )

        # Click the five-star button
        orange_page.click_five_star_button()
        orange_page.click_send_button()

        # Wait for the orange review to be present
        orange_review = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(orange_page.review_div_locator)
        )

        # Get the review rating
        user_rating = orange_page.driver.find_element(*orange_page.review_user_rate).text

        # Assert that the user rating is 5 and the user feedback is correct
        assert user_rating == '(5)'

    finally:
        # Delete the review
        orange_page = OrangePage(driver)
        orange_page.delete_review()