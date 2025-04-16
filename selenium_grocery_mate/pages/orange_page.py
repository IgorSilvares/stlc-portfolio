from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import username, updated_text


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
        self.updated_text_locator = (By.XPATH, f"//div[@class='comment-body']/p[text()='{updated_text}']")
        self.review_options_locator = (By.XPATH, "//div[@class='menu-icon']")
        self.edit_button_locator = (By.XPATH, "//div[@class='dropdown-menu']/button[text()='Edit']")
        self.edit_rating_locator = (By.XPATH, "//input[@type='number']")
        self.edit_text_locator = (By.XPATH, "//div[@class='modal']//textarea")
        self.save_changes_button = (By.XPATH, "//div[@class='modal-buttons']/button[text()='Save Changes']")
        self.delete_button_locator = (By.XPATH, "//div[@class='dropdown-menu']/button[text()='Delete']")
        self.review_div_locator = (By.XPATH, f"//h5/strong[text()='{username}']/ancestor::div[@class='comment-body']")
        self.review_user_rate = (By.XPATH, f"//h5/strong[text()='{username}']/ancestor::div[@class='comment-body']//span[@class='small']")
        self.review_user_feedback = (By.XPATH, f"//h5/strong[text()='{username}']/ancestor::div[@class='comment-body']/p")
        self.review_error_message = (By.XPATH, "//p[@class='error-message']")

    # Actions
    def click_one_star_button(self):
        self.driver.find_element(*self.one_star_locator).click()
    
    def click_two_star_button(self):
        self.driver.find_element(*self.two_star_locator).click()

    def click_three_star_button(self):
        # Wait for the three-star button to be present
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.three_star_locator)
        ).click()

    def click_four_star_button(self):
        self.driver.find_element(*self.four_star_locator).click()

    def click_five_star_button(self):
        # Wait for the five-star button to be present
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.five_star_locator)
        ).click()

    def click_star_rating(self, stars):
        if not 1 <= stars <= 5:
            raise ValueError("Star rating must be between 1 and 5")

        star_locators = {
            1: self.one_star_locator,
            2: self.two_star_locator,
            3: self.three_star_locator,
            4: self.four_star_locator,
            5: self.five_star_locator
        }

        # Wait for the star rating element to be present and click it
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(star_locators[stars])
        ).click()

    def enter_review_text(self, text):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.review_text_locator)
        ).send_keys(text)

    def click_send_button(self):
        self.driver.find_element(*self.send_button_locator).click()

        # Wait for the orange review to be present
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.review_div_locator)
        )
    
    def click_review_options(self):
        self.driver.find_element(*self.review_options_locator).click()
    
    def click_edit_button(self):
        self.driver.find_element(*self.edit_button_locator).click()
    
    def click_delete_button(self):
        self.driver.find_element(*self.delete_button_locator).click()

    def confirm_delete_alert(self):
        self.driver.switch_to.alert.accept()

    def enter_new_rating(self, value):
        self.driver.find_element(*self.edit_rating_locator).clear()
        self.driver.find_element(*self.edit_rating_locator).send_keys(value)

    def enter_new_feedback(self, text):
        self.driver.find_element(*self.edit_text_locator).clear()
        self.driver.find_element(*self.edit_text_locator).send_keys(text)

    def click_save_changes_button(self):
        self.driver.find_element(*self.save_changes_button).click()

        # Wait for the new feedback to be present
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.review_user_feedback)
        )

    def check_feedback_error(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.review_error_message)
            )
            return True  # Error message is present
        except:
            return False  # Error message not found

    def delete_review(self):
        self.driver.find_element(*self.review_div_locator).click()
        self.driver.find_element(*self.review_options_locator).click()
        self.driver.find_element(*self.delete_button_locator).click()
        self.driver.switch_to.alert.accept()

        # Wait for the review to be deleted
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.send_button_locator)
        )
