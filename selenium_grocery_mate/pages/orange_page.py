from selenium.webdriver.common.by import By
from utils.constants import username


class OrangePage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.one_star_locator = (By.XPATH, "//div[@class='interactive-rating']/span[@class='star empty'][1]")
        self.two_star_locator = (By.XPATH, "//div[@class='interactive-rating']/span[@class='star empty'][2]")
        self.three_star_locator = (By.XPATH, "//div[@class='interactive-rating']/span[@class='star empty'][3]")
        self.four_star_locator = (By.XPATH, "//div[@class='interactive-rating']/span[@class='star empty'][4]")
        self.five_star_locator = (By.XPATH, "//div[@class='interactive-rating']/span[@class='star empty'][5]")
        self.review_text_locator = (By.XPATH, "//textarea[@class='new-review-form-control ']")
        self.send_button_locator = (By.XPATH, "//button[@class='new-review-btn new-review-btn-send']")
        self.review_options_locator = (By.XPATH, "//div[@class='menu-icon']")
        self.edit_button_locator = (By.XPATH, "//div[@class='dropdown-menu']/button[text()='Edit']")
        self.delete_button_locator = (By.XPATH, "//div[@class='dropdown-menu']/button[text()='Delete']")
        self.review_div_locator = (By.XPATH, f"//h5/strong[text()='{username}']/ancestor::div[@class='comment-body']")

    # Actions
    def click_edit_button(self):
        self.driver.find_element(*self.edit_button_locator).click()

    def click_checkout(self):
        self.driver.find_element(*self.checkout_locator).click()