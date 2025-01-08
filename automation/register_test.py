import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="function")
def web_driver():
    driver = webdriver.Chrome()
    driver.get("http://automationexercise.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_if_page_is_displayed(web_driver):
    driver = web_driver
    page_logo = driver.find_element(By.XPATH, '//img[@src="/static/images/home/logo.png"]')
    assert page_logo.is_displayed()


def test_new_user_register(web_driver):
    driver = web_driver

    # Close cookies pop up
    cookie_button = driver.find_element(By.XPATH, "//p[text()='Consent']")
    if cookie_button.is_displayed():
        cookie_button.click()

    # Find and interact with signin/login button
    signup_login_button = driver.find_element(By.XPATH, "//a[@href='/login']")
    ActionChains(driver).move_to_element(signup_login_button).click().perform()

    # Verify if is in the New User page
    new_user_text = driver.find_element(By.XPATH, "//h2[text()='New User Signup!']")
    assert new_user_text.is_displayed()

    # Enter new Name and new Email and click signup
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]')
    name_input.send_keys("user")
    email_input.send_keys("user998@user.com")
    signup_button = driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]')
    signup_button.click()

    # Verify that 'ENTER ACCOUNT INFORMATION' is visible
    enter_account_text = driver.find_element(By.XPATH, '//b[text()="Enter Account Information"]')
    assert enter_account_text.is_displayed()

    # Fill details: Title, Name, Email, Password, Date of birth
    mr_title_button = driver.find_element(By.ID, 'id_gender1')
    mr_title_button.click()
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys("password123")
    day_selector = driver.find_element(By.ID, 'days')
    day_selector.click()
    day_option = driver.find_element(By.XPATH, "//option[text()='5']")
    day_option.click()
    month_selector = driver.find_element(By.ID, 'months')
    month_selector.click()
    month_option = driver.find_element(By.XPATH, "//option[text()='March']")
    month_option.click()
    year_selector = driver.find_element(By.ID, 'years')
    year_selector.click()
    year_option = driver.find_element(By.XPATH, "//option[text()='1991']")
    year_option.click()

    # Select checkbox 'Sign up for our newsletter!'
    newsletter_check = driver.find_element(By.ID, 'newsletter')
    newsletter_check.click()

    # Select checkbox 'Receive special offers from our partners!'
    special_offers_check = driver.find_element(By.ID, 'optin')
    special_offers_check.click()

    # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    first_name_input = driver.find_element(By.ID, 'first_name')
    first_name_input.send_keys("User")
    last_name_input = driver.find_element(By.ID, 'last_name')
    last_name_input.send_keys("Resu")
    company_input = driver.find_element(By.ID, 'company')
    company_input.send_keys("User Company")
    address_input = driver.find_element(By.ID, 'address1')
    address_input.send_keys("Street")
    address2_input = driver.find_element(By.ID, 'address2')
    address2_input.send_keys("City")
    country_selector = driver.find_element(By.ID, 'country')
    country_selector.click()
    country_option = driver.find_element(By.XPATH, '//option[text()="Canada"]')
    country_option.click()
    state_input = driver.find_element(By.ID, 'state')
    state_input.send_keys("State")
    city_input = driver.find_element(By.ID, 'city')
    city_input.send_keys("City")
    zipcode_input = driver.find_element(By.ID, 'zipcode')
    zipcode_input.send_keys("123123123")
    mobile_number_input = driver.find_element(By.ID, 'mobile_number')
    mobile_number_input.send_keys("99999999999")

    # Click 'Create Account button'
    create_account_button = driver.find_element(By.XPATH, '//button[@data-qa="create-account"]')
    create_account_button.click()

    # Verify that 'ACCOUNT CREATED!' is visible
    account_created_text = driver.find_element(By.XPATH, '//b[text()="Account Created!"]')
    assert account_created_text.is_displayed()

    # Click 'Continue' button
    continue_button = driver.find_element(By.XPATH, '//a[@data-qa="continue-button"]')
    continue_button.click()

    # Click 'Delete Account' button
    delete_button = driver.find_element(By.XPATH, '//a[@href="/delete_account"]')
    delete_button.click()

    # Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    account_deleted_text = driver.find_element(By.XPATH, '//b[text()="Account Deleted!"]')


if __name__ == "__main__":
    pytest.main()
