from pages.login_page import LoginPage


def test_valid_login(driver):

    login = LoginPage(driver)

    login.open_login_page()

    login.enter_username("admin@slscorp.com")
    login.enter_password("Admin#789")

    login.click_login()

    assert login.is_login_successful()