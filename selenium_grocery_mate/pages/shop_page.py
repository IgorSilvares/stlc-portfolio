from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.age_input_locator = (By.XPATH, "//div[@class='modal-content']/input[@placeholder='DD-MM-YYYY']")
        self.age_confirm_button = (By.XPATH, "//div[@class='modal-content']/button")
        self.orange_locator = (By.XPATH, "//img[@alt='Oranges']")
        self.orange_quantity_locator = (By.XPATH, "//div[@class='card' and .//*[contains(text(),'Oranges')]]//input")
        self.orange_add_to_cart_button = (By.XPATH, "//div[@class='card' and .//*[contains(text(),'Oranges')]]//button[@class='btn btn-primary btn-cart']")
        self.search_input_locator = (By.XPATH, "//input[@type='text' and @placeholder='Search Products']")

    # Actions
    def enter_orange_quantity(self, quantity):
        self.driver.find_element(*self.orange_quantity_locatorr).send_keys(quantity)

    def enter_age(self, age):
        self.driver.find_element(*self.checkout_locator).send_keys(age)

    def enter_search(self, search):
        self.driver.find_element(*self.search_input_locator).send_keys(search)
    
    def click_age_confirm_button(self):
        self.driver.find_element(*self.age_confirm_button).click()
    
    def click_orange_add_to_cart_button(self):
        self.driver.find_element(*self.orange_add_to_cart_button).click()

    def click_orange(self):
        self.driver.find_element(*self.orange_locator).click()