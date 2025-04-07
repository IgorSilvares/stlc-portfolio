from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.shop_page import ShopPage
from . import shop_page
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

        # Initialize ShopPage first to access its locators
        shop_page = ShopPage(self.driver)

        # Wait for a shop page element to be present
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(shop_page.search_input_locator)
        )

        return shop_page

    def click_checkout(self):
        self.driver.find_element(*self.checkout_locator).click()
        return CheckoutPage()