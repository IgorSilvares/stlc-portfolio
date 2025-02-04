from ..pages.login_page import LoginPage
from ..utils.constants import user, password
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page('https://grocerymate.masterschool.com/auth')
    login_page.enter_email(user)
    login_page.enter_password(password)
    login_page.click_sign_in_button()

    WebDriverWait(driver, 3).until(
        EC.url_to_be('https://grocerymate.masterschool.com/')
    )

    assert login_page.driver.current_url == 'https://grocerymate.masterschool.com/'