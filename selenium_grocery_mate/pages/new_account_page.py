from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class NewAccountPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.full_name_locator = (By.XPATH, "//input[@placeholder='Full Name']")
        self.email_locator = (By.XPATH, "//input[@placeholder='Email address']")
        self.password_locator = (By.XPATH, "//input[@placeholder='Password']")
        self.sign_up_button = (By.XPATH, "//button[@class='submit-btn']")

    # Actions
    def enter_name(self, name):
        # Wait for the homepage to be loaded
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.full_name_locator)
        )
        self.driver.find_element(*self.full_name_locator).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_locator).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_sign_up(self):
        self.driver.find_element(*self.sign_up_button).click()

    def create_account(self, name, email, password):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_up()
