import time
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.new_account_page import NewAccountPage


def generate_random_string(length=8):
    """Generate random string of lowercase letters"""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_random_email():
    """Generate unique email with timestamp"""
    return f"testuser_{generate_random_string(6)}_{int(time.time())}@example.com"


# Random test data
NEW_USER_NAME = f"User_{generate_random_string(6)}"
NEW_EMAIL = generate_random_email()
NEW_PASSWORD = f"Pwd_{generate_random_string(8)}!"


def test_account_registration_and_login(driver):
    print(f"Testing with:\nUsername: {NEW_USER_NAME}\nEmail: {NEW_EMAIL}\nPassword: {NEW_PASSWORD}")

    # Navigate to registration page
    login_page = LoginPage(driver)
    login_page.open_page()

    # Create new account with explicit waits
    new_account_page = login_page.click_create_new_account_button()
    new_account_page.create_account(NEW_USER_NAME, NEW_EMAIL, NEW_PASSWORD)

    # Login with new credentials
    login_page.open_page_and_login(NEW_EMAIL, NEW_PASSWORD)

    assert login_page.driver.current_url == 'https://grocerymate.masterschool.com/'
