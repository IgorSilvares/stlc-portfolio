from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.email_locator = (By.XPATH, "//input[@type='email']")
        self.password_locator = (By.XPATH, "//input[@type='password']")
        self.sign_in__button_locator = (By.XPATH, "//button[@type='submit']")	


    # Actions
    def open_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        self.driver.find_element(*self.email_locator).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in__button_locator).click()