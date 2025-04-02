from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlcoholPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.product_grid_locator = (By.XPATH, "//div[@class='product-grid']")
        self.no_product_locator = (By.XPATH, "//div[@class='no-products-card']")
        self.underage_message_locator = (By.XPATH, "//h2[text()='Underage Notice']")

    # Actions
    def is_underage_message_visible(self, timeout=1):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.underage_message_locator)
            )
            return True
        except TimeoutException:
            return False