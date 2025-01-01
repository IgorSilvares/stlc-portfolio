import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="function")
def web_driver():
    driver = webdriver.Chrome()
    driver.get("http://automationexercise.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


# def test_if_page_is_displayed(web_driver):
#     driver = web_driver
#     page_logo = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[1]/div/a/img')
#     assert page_logo.is_displayed()


def test_new_user_register(web_driver):
    driver = web_driver

    # Close cookies pop up
    cookie_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]/p")
    if cookie_button.is_displayed():
        cookie_button.click()

    # Find and interact with signin/login button
    signup_login_button = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    ActionChains(driver).move_to_element(signup_login_button).click().perform()

    # Verify if is in the New User page
    new_user_text = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/h2")
    assert new_user_text.is_displayed()

    # Enter new Name and new Email and click signup
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
    name_input.send_keys("user")
    email_input.send_keys("user998@user.com")
    signup_button = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button')
    signup_button.click()

    # Verify that 'ENTER ACCOUNT INFORMATION' is visible
    enter_account_text = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/h2/b')
    assert enter_account_text.is_displayed()

    # Fill details: Title, Name, Email, Password, Date of birth
    mr_title_button = driver.find_element(By.XPATH, '//*[@id="id_gender1"]')
    mr_title_button.click()
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys("password123")
    day_selector = driver.find_element(By.XPATH, '//*[@id="days"]')
    day_selector.click()
    day_option = driver.find_element(By.XPATH, "//option[text()='5']")
    day_option.click()
    month_selector = driver.find_element(By.XPATH, '//*[@id="months"]')
    month_selector.click()
    month_option = driver.find_element(By.XPATH, "//option[text()='March']")
    month_option.click()
    year_selector = driver.find_element(By.XPATH, '//*[@id="years"]')
    year_selector.click()
    year_option = driver.find_element(By.XPATH, "//option[text()='1991']")
    year_option.click()

    # Select checkbox 'Sign up for our newsletter!'
    newsletter_check = driver.find_element(By.XPATH, '//*[@id="newsletter"]')
    newsletter_check.click()

    # Select checkbox 'Receive special offers from our partners!'
    special_offers_check = driver.find_element(By.XPATH, '//*[@id="optin"]')
    special_offers_check.click()

    # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    first_name_input = driver.find_element(By.XPATH, '//*[@id="first_name"]')
    first_name_input.send_keys("User")
    last_name_input = driver.find_element(By.XPATH, '//*[@id="last_name"]')
    last_name_input.send_keys("Resu")
    company_input = driver.find_element(By.XPATH, '//*[@id="company"]')
    company_input.send_keys("User Company")
    address_input = driver.find_element(By.XPATH, '//*[@id="address1"]')
    address_input.send_keys("Street")
    address2_input = driver.find_element(By.XPATH, '//*[@id="address2"]')
    address2_input.send_keys("City")
    country_selector = driver.find_element(By.XPATH, '//*[@id="country"]')
    country_selector.click()
    country_option = driver.find_element(By.XPATH, '//option[text()="Canada"]')
    country_option.click()
    state_input = driver.find_element(By.XPATH, '//*[@id="state"]')
    state_input.send_keys("State")
    city_input = driver.find_element(By.XPATH, '//*[@id="city"]')
    city_input.send_keys("City")
    zipcode_input = driver.find_element(By.XPATH, '//*[@id="zipcode"]')
    zipcode_input.send_keys("123123123")
    mobile_number_input = driver.find_element(By.XPATH, '//*[@id="mobile_number"]')
    mobile_number_input.send_keys("99999999999")

    # Click 'Create Account button'
    create_account_button = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/button')
    create_account_button.click()

    # Verify that 'ACCOUNT CREATED!' is visible
    account_created_text = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/h2/b')
    assert account_created_text.is_displayed()

    # Click 'Continue' button
    continue_button = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a')
    continue_button.click()

    # Click 'Delete Account' button
    delete_button = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
    delete_button.click()

    # Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    account_deleted_text = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/h2/b')


if __name__ == "__main__":
    pytest.main()
