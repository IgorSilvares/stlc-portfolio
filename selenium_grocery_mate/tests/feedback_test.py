from pages.login_page import LoginPage
from pages.orange_page import OrangePage
from utils.constants import user, password, feedback_100char, feedback_500char


def _login_and_navigate_to_item(driver, search_term):
    # Login with user and password
    homepage = LoginPage(driver).open_page_and_login(user, password)

    # Enter the Shop Page
    shop_page = homepage.click_shop()
    shop_page.click_age_confirm_button()

    # Search for the product
    shop_page.enter_search(search_term)

    # Enter the product page
    return shop_page.click_searched_item()


def _test_feedback(driver, feedback_text, stars=None, expected_rating=None, expect_error=False):
    orange_page = None
    try:
        orange_page = _login_and_navigate_to_item(driver, "oranges")
        orange_page.enter_review_text(feedback_text)

        if not expect_error:
            # Dynamically call the correct star-rating method
            getattr(orange_page, f"click_{stars}_star_button")()
            # Click the send button
            orange_page.click_send_button()

            # Get the user rating
            user_rating = orange_page.driver.find_element(*orange_page.review_user_rate).text

            # Assert the user rating is the expected
            user_feedback = orange_page.driver.find_element(*orange_page.review_user_feedback).text
            assert user_rating == f'({expected_rating})'
            assert user_feedback == feedback_text
        else:
            assert orange_page.check_feedback_error()

    finally:
        if not expect_error and orange_page:
            OrangePage(driver).delete_review()


# Test cases
def test_100char_feedback_with_3_stars(driver):
    _test_feedback(driver, feedback_100char, stars="three", expected_rating=3)


def test_500char_feedback_error(driver):
    _test_feedback(driver, feedback_500char, expect_error=True)
