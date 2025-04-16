import pytest
from pages.login_page import LoginPage
from pages.orange_page import OrangePage
from utils.constants import user, password, feedback_100char, feedback_500char


def _login_and_navigate_to_item(driver, search_term):
    """Login and navigate to specified product page"""
    homepage = LoginPage(driver).open_page_and_login(user, password)
    shop_page = homepage.click_shop()
    shop_page.click_age_confirm_button()
    shop_page.enter_search(search_term)
    return shop_page.click_searched_item()


@pytest.mark.parametrize("feedback_text,stars,expect_error", [
    # Valid 100 character feedback with 3 stars
    pytest.param(
        feedback_100char,
        3,
        False
    ),
    # Invalid 500 character feedback (expect error)
    pytest.param(
        feedback_500char,
        None,
        True
    )
])
def test_feedback_submission(driver, feedback_text, stars, expect_error):
    orange_page = None
    try:
        # Setup test
        orange_page = _login_and_navigate_to_item(driver, "oranges")
        orange_page.enter_review_text(feedback_text)

        if not expect_error:
            # Call the star-rating method
            orange_page.click_star_rating(stars)
            orange_page.click_send_button()

            # Verify submission
            user_rating = orange_page.driver.find_element(*orange_page.review_user_rate).text
            user_feedback = orange_page.driver.find_element(*orange_page.review_user_feedback).text

            assert user_rating == f'({stars})'

            assert user_feedback == feedback_text

        else:
            # Verify error case
            assert orange_page.check_feedback_error()

    finally:
        # Cleanup - only delete if it was a successful submission
        if orange_page and not expect_error:
            OrangePage(driver).delete_review()
