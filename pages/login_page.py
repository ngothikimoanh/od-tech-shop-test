from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    phone_number_input = (By.NAME, "phone_number")
    password_input = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR,".btn.btn-primary")
    error_message = (By.CSS_SELECTOR, ".text-danger")


    def enter_phone_number(self, phone_number):
        self.send_keys(self.phone_number_input, phone_number)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def get_error_message(self):
        self.find_element(self.error_message)