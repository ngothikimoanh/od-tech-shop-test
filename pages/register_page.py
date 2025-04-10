from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    phone_number_input = (By.ID, "phone_number")
    password_input = (By.ID, "password")
    confirm_password_input = (By.ID, "password_confirm")
    register_button = (By.ID, "register_submit_btn")

    def __init__(self, driver, config, timeout=10):
        super().__init__(driver, config, timeout)
        driver.get(self.base_url + "auth/register")

    def enter_phone_number(self, phone_number):
        self.send_keys(self.phone_number_input, phone_number)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def enter_confirm_password(self, confirm_password):
        self.send_keys(self.confirm_password_input, confirm_password)

    def click_register(self):
        self.click(self.register_button)
