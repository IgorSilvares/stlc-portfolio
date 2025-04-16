from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.orange_page import OrangePage
from pages.alcohol_page import AlcoholPage
from pages.checkout_page import CheckoutPage


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

        WebDriverWait(self.driver, 3).until(
            EC.url_to_be('https://grocerymate.masterschool.com/store')
        )

        # Locators
        self.age_input_locator = (By.XPATH, "//div[@class='modal-content']/input[@placeholder='DD-MM-YYYY']")
        self.age_confirm_button = (By.XPATH, "//div[@class='modal-content']/button")
        self.orange_locator = (By.XPATH, "//img[@alt='Oranges']")
        self.orange_quantity_locator = (By.XPATH, "//div[@class='card' and .//*[contains(text(),'Oranges')]]//input")
        self.orange_add_to_cart_button = (By.XPATH,
                                          "//div[@class='card' and .//*[contains(text(),'Oranges')]]//button["
                                          "@class='btn btn-primary btn-cart']")
        self.search_input_locator = (By.XPATH, "//input[@type='text' and @placeholder='Search Products']")
        self.searched_item_locator = (By.XPATH, "//div[@class='suggestion-item']")
        self.alcohol_locator = (By.XPATH, "//a[text()='Alocohol']")
        self.celery_quantity_locator = (By.XPATH, "//div[@class='card' and .//*[contains(text(),'Celery')]]//input")
        self.celery_add_to_cart_button = (By.XPATH, "//div[@class='card' and .//*[contains(text(),"
                                                    "'Celery')]]//button[@class='btn btn-primary btn-cart']")
        self.checkout_button = (By.XPATH, "//div[@class='headerIcon'][3]")
        self.next_button = (By.XPATH, "//button[@class='pagination-link' and .//text()='Next']")

        self.first_product_quantity = (By.XPATH, "(//input[@class='quantity'])[1]")
        self.first_product_add_button = (By.XPATH, "(//button[@class='btn btn-primary btn-cart'])[1]")

    # Actions
    def enter_celery_quantity(self, quantity):
        self.driver.find_element(*self.celery_quantity_locator).clear()
        self.driver.find_element(*self.celery_quantity_locator).send_keys(quantity)

    def enter_age(self, age):
        self.driver.find_element(*self.age_input_locator).send_keys(age)

        # Wait for value to be populated
        WebDriverWait(self.driver, 3).until(
            EC.text_to_be_present_in_element_value(
                self.age_input_locator,
                age
            )
        )

    def enter_search(self, search):
        self.driver.find_element(*self.search_input_locator).send_keys(search)

        WebDriverWait(self.driver, timeout=3).until(
            EC.presence_of_element_located(self.searched_item_locator)
        )

    def click_searched_item(self):
        # Wait for and click the item
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.searched_item_locator)
        ).click()

        # Return the OrangePage
        return OrangePage(self.driver)

    def click_age_confirm_button(self):
        self.driver.find_element(*self.age_confirm_button).click()

    def click_celery_add_to_cart_button(self):
        self.driver.find_element(*self.celery_add_to_cart_button).click()

    def click_orange(self):
        self.driver.find_element(*self.orange_locator).click()
        return OrangePage(self.driver)

    def click_alcohol(self):
        # Wait for the alcohol link to be present
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.alcohol_locator)
        ).click()
        return AlcoholPage(self.driver)

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def click_first_product_add_to_cart(self):
        self.driver.find_element(*self.first_product_add_button).click()

    def enter_first_product_quantity(self, quantity):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.first_product_quantity)
        )
        self.driver.find_element(*self.first_product_quantity).clear()
        self.driver.find_element(*self.first_product_quantity).send_keys(quantity)
