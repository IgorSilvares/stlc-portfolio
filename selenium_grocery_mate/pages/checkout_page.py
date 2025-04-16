from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.remove_product_locator = (By.XPATH, "//a[@class='remove-icon']")
        self.shipment_price_locator = (By.XPATH, "//div[@class='shipment-container']//h5[2]")
        self.plus_product_button = (By.XPATH, "//button[@class='plus']")
        self.minus_product_button = (By.XPATH, "//button[@class='minus']")
        self.remove_all_button = (By.XPATH, "//a[@class='remove-icon']")

    # Actions
    def click_remove_product(self):
        self.driver.find_element(*self.remove_product_locator).click()

    def get_shipment_price(self):
        return WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.shipment_price_locator)
        )

    def click_remove_all_button(self):
        self.driver.find_element(*self.remove_all_button).click()

    def click_plus_product_button(self):
        self.driver.find_element(*self.plus_product_button).click()

    def click_minus_product_button(self):
        self.driver.find_element(*self.minus_product_button).click()
