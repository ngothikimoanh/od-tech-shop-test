from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    phone_number_input = (By.ID, "phone_number")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login_submit_btn")

    def __init__(self, driver, config, timeout=10):
        super().__init__(driver, config, timeout)

        driver.get(self.base_url + "auth/login")

    def enter_phone_number(self, phone_number):
        self.send_keys(self.phone_number_input, phone_number)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)
