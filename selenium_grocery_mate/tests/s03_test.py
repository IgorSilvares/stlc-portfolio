from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.orange_page import OrangePage
from pages.shop_page import ShopPage
from utils.constants import user, password, feedback_100char

def test_three_star(driver):
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

        # Wait for the orange element to be present
        orange_element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(shop_page.orange_locator)
        )

        # Click the orange element
        shop_page.click_orange()
        orange_page = OrangePage(driver)

        # Wait for the five-star button to be present
        five_star_button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(orange_page.five_star_locator)
        )

        # Enter review text
        orange_page.enter_review_text(feedback_100char)

        # Click the three-star button
        orange_page.click_three_star_button()
        orange_page.click_send_button()

        # Wait for the orange review to be present
        orange_review = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(orange_page.review_div_locator)
        )

        # Get the review rating
        user_rating = orange_page.driver.find_element(*orange_page.review_user_rate).text
        user_feedback = orange_page.driver.find_element(*orange_page.review_user_feedback).text

        # Assert that the user rating is 3 and the user feedback is correct
        assert user_rating == '(3)'
        assert user_feedback == feedback_100char

    finally:
        # Delete the review (executed regardless of the test result)
        orange_page = OrangePage(driver)
        orange_page.delete_review()