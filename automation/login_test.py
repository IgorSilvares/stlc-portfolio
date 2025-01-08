import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def web_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.mark.parametrize("username", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
])
def test_login(web_driver, username):
    driver = web_driver
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.clear()
    password_input.clear()
    username_input.send_keys(username)
    password_input.send_keys("secret_sauce")
    login_button.click()

    product_title = driver.find_element(By.CLASS_NAME, "title")
    assert "PRODUCTS" in product_title.text.upper()


def test_verify_product(web_driver):
    driver = web_driver
    product_name = "Sauce Labs Backpack"
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    product_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{product_name}']")))
    assert product_element is not None, f"Product '{product_name}' not found on the products page"
    print(f"Product '{product_name}' is displayed on the products page.")


if __name__ == "__main__":
    pytest.main()
