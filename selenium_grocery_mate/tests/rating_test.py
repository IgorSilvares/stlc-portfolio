from pages.login_page import LoginPage
from pages.orange_page import OrangePage
from utils.constants import user, password


def _login_and_navigate_to_item(driver, search_term):
    # Login with user and password
    homepage = LoginPage(driver).open_page_and_login(user, password)

    # Enter the Shop Page
    shop_page = homepage.click_shop()
    shop_page.click_age_confirm_button()

    # Search for the product
    shop_page.enter_search(search_term)

    # Enter the product page
    shop_page.click_searched_item()

    return shop_page.click_searched_item()


def _test_star_rating(driver, stars, expected_rating):
    orange_page = None
    try:
        orange_page = _login_and_navigate_to_item(driver, "oranges")

        # Dynamically call the correct star-rating method
        getattr(orange_page, f"click_{stars}_star_button")()
        # Click the send button
        orange_page.click_send_button()

        # Get the user rating
        user_rating = orange_page.driver.find_element(*orange_page.review_user_rate).text
        # Assert the user rating is the expected
        assert user_rating == f'({expected_rating})'

    finally:
        # Delete the review
        if orange_page:
            OrangePage(driver).delete_review()


def test_five_star(driver):
    _test_star_rating(driver, "five", 5)


def test_three_star(driver):
    _test_star_rating(driver, "three", 3)
