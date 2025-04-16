import pytest
from pages.login_page import LoginPage
from utils.constants import user, password

# Test cases for age validation
AGE_TEST_CASES = [
    # (birthdate, is_valid_age, test_description)
    ("01-01-2000", True, "valid_age_of_23"),
    ("01-01-2020", False, "invalid_age_of_3"),
    ("", False, "empty_age_field")
]


@pytest.mark.parametrize("birthdate,is_valid_age,test_description", AGE_TEST_CASES)
def test_age_validation(driver, birthdate, is_valid_age, test_description):
    """Tests age validation for alcohol purchase"""

    # Login with user credentials
    homepage = LoginPage(driver).open_page_and_login(user, password)

    # Navigate to shop page
    shop_page = homepage.click_shop()

    # Enter birthdate
    shop_page.enter_age(birthdate)

    # Confirm age and proceed to alcohol section
    shop_page.click_age_confirm_button()
    alcohol_page = shop_page.click_alcohol()

    # Verify underage message visibility matches expectations
    if is_valid_age:
        assert not alcohol_page.is_underage_message_visible()
    else:
        assert alcohol_page.is_underage_message_visible()
