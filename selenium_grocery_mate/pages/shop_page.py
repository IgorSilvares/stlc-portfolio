from selenium.webdriver.common.by import By
from pages.orange_page import OrangePage
from pages.alcohol_page import AlcoholPage
from pages.checkout_page import CheckoutPage


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.age_input_locator = (By.XPATH, "//div[@class='modal-content']/input[@placeholder='DD-MM-YYYY']")
        self.age_confirm_button = (By.XPATH, "//div[@class='modal-content']/button")
        self.orange_locator = (By.XPATH, "//img[@alt='Oranges']")
        self.orange_quantity_locator = (By.XPATH, "//div[@class='card' and .//*[contains(text(),'Oranges')]]//input")
        self.orange_add_to_cart_button = (By.XPATH, "//div[@class='card' and .//*[contains(text(),'Oranges')]]//button[@class='btn btn-primary btn-cart']")
        self.search_input_locator = (By.XPATH, "//input[@type='text' and @placeholder='Search Products']")
        self.searched_item_locator = (By.XPATH, "//div[@class='suggestion-item']")
        self.alcohol_locator = (By.XPATH, "//a[text()='Alocohol']")
        self.celery_quantity_locator = (By.XPATH, "//div[@class='card' and .//*[contains(text(),'Celery')]]//input")
        self.celery_add_to_cart_button = (By.XPATH, "//div[@class='card' and .//*[contains(text(),'Celery')]]//button[@class='btn btn-primary btn-cart']")
        self.checkout_button = (By.XPATH, "//div[@class='headerIcon'][3]")

    # Actions

    def enter_celery_quantity(self, quantity):
        self.driver.find_element(*self.celery_quantity_locator).clear()
        self.driver.find_element(*self.celery_quantity_locator).send_keys(quantity)

    def enter_age(self, age):
        self.driver.find_element(*self.age_input_locator).send_keys(age)

    def enter_search(self, search):
        self.driver.find_element(*self.search_input_locator).send_keys(search)

    def click_searched_item(self):
        self.driver.find_element(*self.searched_item_locator).click()
    
    def click_age_confirm_button(self):
        self.driver.find_element(*self.age_confirm_button).click()
    
    def click_celery_add_to_cart_button(self):
        self.driver.find_element(*self.celery_add_to_cart_button).click()

    def click_orange(self):
        self.driver.find_element(*self.orange_locator).click()
        return OrangePage(self.driver)

    def click_alcohol(self):
        self.driver.find_element(*self.alcohol_locator).click()
        return AlcoholPage(self.driver)

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)