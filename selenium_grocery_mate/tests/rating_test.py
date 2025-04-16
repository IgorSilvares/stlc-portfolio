import pytest
from pages.login_page import LoginPage
from pages.orange_page import OrangePage
from utils.constants import user, password


def _login_and_navigate_to_item(driver, search_term):
    homepage = LoginPage(driver).open_page_and_login(user, password)
    shop_page = homepage.click_shop()
    shop_page.click_age_confirm_button()
    shop_page.enter_search(search_term)
    return shop_page.click_searched_item()


@pytest.mark.parametrize("stars", [
    5,
    3,
])
def test_star_ratings(driver, stars):
    orange_page = None
    try:
        # Setup test
        orange_page = _login_and_navigate_to_item(driver, "oranges")

        # Select star rating dynamically
        orange_page.click_star_rating(stars)
        orange_page.click_send_button()

        # Verify rating was saved correctly
        user_rating = orange_page.driver.find_element(*orange_page.review_user_rate).text
        assert user_rating == f'({stars})'

    finally:
        # Cleanup
        if orange_page:
            OrangePage(driver).delete_review()