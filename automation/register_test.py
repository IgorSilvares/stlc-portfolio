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


@pytest.mark.parametrize("name, email, password, title, birth_day, birth_month, birth_year, first_name, last_name, "
                         "company, address1, address2, country, state, city, zipcode, mobile_number", [
    ("user", "user998@user.com", "password123", "Mr", "5", "March", "1991", "User", "Resu", "User Company", "Street", "City", "Canada", "State", "City", "123123123", "99999999999"),
])
def test_new_user_register(web_driver, name, email, password, title, birth_day, birth_month, birth_year, first_name, last_name, company, address1, address2, country, state, city, zipcode, mobile_number):
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
    name_input.send_keys(name)
    email_input.send_keys(email)
    signup_button = driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]')
    signup_button.click()

    # Verify that 'ENTER ACCOUNT INFORMATION' is visible
    enter_account_text = driver.find_element(By.XPATH, '//b[text()="Enter Account Information"]')
    assert enter_account_text.is_displayed()

    # Fill details: Title, Password, Date of birth
    if title == "Mr":
        driver.find_element(By.ID, 'id_gender1').click()
    else:
        driver.find_element(By.ID, 'id_gender2').click()

    driver.find_element(By.ID, 'password').send_keys(password)

    driver.find_element(By.ID, 'days').click()
    driver.find_element(By.XPATH, f"//option[text()='{birth_day}']").click()

    driver.find_element(By.ID, 'months').click()
    driver.find_element(By.XPATH, f"//option[text()='{birth_month}']").click()

    driver.find_element(By.ID, 'years').click()
    driver.find_element(By.XPATH, f"//option[text()='{birth_year}']").click()

    # Select checkboxes
    driver.find_element(By.ID, 'newsletter').click()
    driver.find_element(By.ID, 'optin').click()

    # Fill personal details
    driver.find_element(By.ID, 'first_name').send_keys(first_name)
    driver.find_element(By.ID, 'last_name').send_keys(last_name)
    driver.find_element(By.ID, 'company').send_keys(company)
    driver.find_element(By.ID, 'address1').send_keys(address1)
    driver.find_element(By.ID, 'address2').send_keys(address2)

    driver.find_element(By.ID, 'country').click()
    driver.find_element(By.XPATH, f'//option[text()="{country}"]').click()

    driver.find_element(By.ID, 'state').send_keys(state)
    driver.find_element(By.ID, 'city').send_keys(city)
    driver.find_element(By.ID, 'zipcode').send_keys(zipcode)
    driver.find_element(By.ID, 'mobile_number').send_keys(mobile_number)

    # Click 'Create Account' button
    driver.find_element(By.XPATH, '//button[@data-qa="create-account"]').click()

    # Verify 'ACCOUNT CREATED!' is visible
    assert driver.find_element(By.XPATH, '//b[text()="Account Created!"]').is_displayed()

    # Click 'Continue' and 'Delete Account' buttons
    driver.find_element(By.XPATH, '//a[@data-qa="continue-button"]').click()
    driver.find_element(By.XPATH, '//a[@href="/delete_account"]').click()

    # Verify 'ACCOUNT DELETED!' is visible
    assert driver.find_element(By.XPATH, '//b[text()="Account Deleted!"]').is_displayed()
