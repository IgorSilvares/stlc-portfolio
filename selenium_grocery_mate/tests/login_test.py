from pages.login_page import LoginPage
from utils.constants import user, password


def test_login(driver):
    homepage = LoginPage(driver).open_page_and_login(user, password)

    assert homepage.driver.current_url == 'https://grocerymate.masterschool.com/'

