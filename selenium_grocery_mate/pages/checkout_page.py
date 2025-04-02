from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.remove_product_locator = (By.XPATH, "//a[@class='remove-icon']")
        self.shipment_price_locator = (By.XPATH, "//div[@class='shipment-container']//h5[2]")

    # Actions
    def click_remove_product(self):
        self.driver.find_element(*self.remove_product_locator).click()