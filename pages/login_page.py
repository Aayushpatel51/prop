from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Locators
    email = (By.CSS_SELECTOR, '[formcontrolname="email"]')
    password = (By.CSS_SELECTOR, '[formcontrolname="password"]')
    login_button = (By.CSS_SELECTOR, '[type="submit"]')
    dashboard_text = (By.XPATH, "//span[text()='Dashboard']")

    # Actions
    def open_login_page(self):
        self.driver.get("https://appuat.propmaintain.co.uk/")

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.email)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def is_login_successful(self):
        return self.wait.until(EC.visibility_of_element_located(self.dashboard_text)).is_displayed()