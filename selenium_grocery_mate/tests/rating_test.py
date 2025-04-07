from pages.login_page import LoginPage
from pages.orange_page import OrangePage
from utils.constants import user, password


def login_and_navigate_to_item(driver, search_term):
    # Login with user and password
    homepage = LoginPage(driver).open_page_and_login(user, password)

    # Enter the Shop Page
    shop_page = homepage.click_shop()
    shop_page.click_age_confirm_button()

    # Search for the product
    shop_page.enter_search(search_term)

    # Enter the product page
    orange_page = shop_page.click_searched_item()

    return orange_page


def test_five_star(driver):
    try:
        # Login and navigate to the orange item
        orange_page = login_and_navigate_to_item(driver, "oranges")

        # Click the five-star button
        orange_page.click_five_star_button()

        # Click the send button
        orange_page.click_send_button()

        # Get the review rating
        user_rating = orange_page.driver.find_element(*orange_page.review_user_rate).text

        # Assert that the user rating is 5 and the user feedback is correct
        assert user_rating == '(5)'

    finally:
        # Delete the review
        orange_page = OrangePage(driver)
        orange_page.delete_review()


def test_three_star(driver):
    try:
        # Login and navigate to the orange item
        orange_page = login_and_navigate_to_item(driver, "oranges")

        # Click the three-star button
        orange_page.click_three_star_button()
        orange_page.click_send_button()

        # Get the review rating
        user_rating = orange_page.driver.find_element(*orange_page.review_user_rate).text

        # Assert that the user rating is 3 and the user feedback is correct
        assert user_rating == '(3)'

    finally:
        # Delete the review
        orange_page = OrangePage(driver)
        orange_page.delete_review()
