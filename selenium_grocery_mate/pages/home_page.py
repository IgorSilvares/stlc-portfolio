from selenium.webdriver.common.by import By
from pages.shop_page import ShopPage
from .checkout_page import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.shop_locator = (By.XPATH, "//li/a[@href='/store']")
        self.checkout_locator = (By.XPATH, "//div[@class='headerIcon'][3]")

    # Actions
    def click_shop(self):
        # Click the shop button
        self.driver.find_element(*self.shop_locator).click()
        return ShopPage(self.driver)

    def click_checkout(self):
        self.driver.find_element(*self.checkout_locator).click()
        return CheckoutPage(self.driver)
