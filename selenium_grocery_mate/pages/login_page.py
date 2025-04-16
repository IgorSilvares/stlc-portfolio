from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.home_page import HomePage
from utils.constants import log_in_url


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.email_locator = (By.XPATH, "//input[@type='email']")
        self.password_locator = (By.XPATH, "//input[@type='password']")
        self.sign_in__button_locator = (By.XPATH, "//button[@type='submit']")	

    # Actions
    def open_page(self):
        self.driver.get(log_in_url)

    def enter_email(self, email):
        self.driver.find_element(*self.email_locator).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in__button_locator).click()
        return HomePage(self.driver)

    def open_page_and_login(self, email, password):
        self.open_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in_button()

        # Wait for the homepage to be loaded
        WebDriverWait(self.driver, 3).until(
            EC.url_to_be('https://grocerymate.masterschool.com/')
        )

        return HomePage(self.driver)
