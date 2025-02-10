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
        self.review_user_rate = (By.XPATH, f"//h5/strong[text()='{username}']/ancestor::div[@class='comment-body']//span[@class='small']")

    # Actions
    def click_one_star_button(self):
        self.driver.find_element(*self.one_star_locator).click()
    
    def click_two_star_button(self):
        self.driver.find_element(*self.two_star_locator).click()

    def click_three_star_button(self):
        self.driver.find_element(*self.three_star_locator).click()
    
    def click_four_star_button(self):
        self.driver.find_element(*self.four_star_locator).click()

    def click_five_star_button(self):
        self.driver.find_element(*self.five_star_locator).click()

    def enter_review_text(self, text):
        self.driver.find_element(*self.review_text_locator).send_keys(text)

    def click_send_button(self):
        self.driver.find_element(*self.send_button_locator).click()
    
    def click_review_options(self):
        self.driver.find_element(*self.review_options_locator).click()
    
    def click_edit_button(self):
        self.driver.find_element(*self.edit_button_locator).click()
    
    def click_delete_button(self):
        self.driver.find_element(*self.delete_button_locator).click()

    def confirm_delete_alert(self):
        self.driver.switch_to.alert.accept()