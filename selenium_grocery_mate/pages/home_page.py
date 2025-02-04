from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.shop_locator = (By.XPATH, "//li/a[@href='/store']")
        self.checkout_locator = (By.XPATH, "//div[@class='headerIcon'][3]")
        

    # Actions
    def click_shop(self):
        self.driver.find_element(*self.shop_locator).click()

    def click_checkout(self):
        self.driver.find_element(*self.checkout_locator).click()