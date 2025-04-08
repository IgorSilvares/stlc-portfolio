from pages.login_page import LoginPage
from utils.constants import user, password


def _age_test_helper(driver, birth_date, valid_age):
    """Helper function for age verification tests"""

    # Login with user and password
    homepage = LoginPage(driver).open_page_and_login(user, password)

    # Enter the Shop Page
    shop_page = homepage.click_shop()

    # Enter the birthdate
    shop_page.enter_age(birth_date)

    # Click the confirm button
    shop_page.click_age_confirm_button()
    alcohol_page = shop_page.click_alcohol()

    if valid_age:
        assert not alcohol_page.is_underage_message_visible()
    else:
        assert alcohol_page.is_underage_message_visible()


def test_valid_age(driver):
    _age_test_helper(driver, "01-01-2000", valid_age=True)


def test_invalid_age(driver):
    _age_test_helper(driver, "01-01-2020", valid_age=False)


def test_empty_age(driver):
    _age_test_helper(driver, birth_date="", valid_age=False)