import pytest
from pages.login_page import LoginPage
from pages.orange_page import OrangePage
from utils.constants import user, password, feedback_100char, updated_text

# Test data for review editing
REVIEW_TEST_CASES = [
    {
        "search_term": "oranges",
        "initial_feedback": feedback_100char,
        "initial_rating": 3,
        "updated_feedback": updated_text,
        "updated_rating": 4,
        "test_description": "edit_review_with_valid_data"
    }
]


def _login_and_navigate_to_item(driver, search_term):
    """Login and navigate to specified product page"""
    homepage = LoginPage(driver).open_page_and_login(user, password)
    shop_page = homepage.click_shop()
    shop_page.click_age_confirm_button()
    shop_page.enter_search(search_term)
    return shop_page.click_searched_item()


def _delete_review(driver):
    """Clean up by deleting the review"""
    OrangePage(driver).delete_review()


@pytest.mark.parametrize("test_data", REVIEW_TEST_CASES)
def test_edit_review(driver, test_data):
    """Test editing product reviews with various parameters"""
    try:
        # Setup: Navigate to product and create initial review
        orange_page = _login_and_navigate_to_item(driver, test_data["search_term"])
        orange_page.enter_review_text(test_data["initial_feedback"])
        orange_page.click_star_rating(test_data["initial_rating"])
        orange_page.click_send_button()

        # Get initial review details
        initial_rating = orange_page.driver.find_element(*orange_page.review_user_rate).text
        initial_feedback = orange_page.driver.find_element(*orange_page.review_user_feedback).text

        # Edit the review
        orange_page.click_review_options()
        orange_page.click_edit_button()
        orange_page.enter_new_rating(test_data["updated_rating"])
        orange_page.enter_new_feedback(test_data["updated_feedback"])
        orange_page.click_save_changes_button()

        # Verify changes
        updated_rating = orange_page.driver.find_element(*orange_page.review_user_rate).text
        updated_feedback = orange_page.driver.find_element(*orange_page.review_user_feedback).text

        assert updated_feedback == test_data["updated_feedback"]

        assert updated_rating == f"({test_data['updated_rating']})"

        assert updated_feedback != initial_feedback

        assert updated_rating != initial_rating

    finally:
        # Teardown
        _delete_review(driver)
