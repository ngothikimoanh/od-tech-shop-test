from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login")

    def enter_username(self, username):
        self.send_keys(self.username_input, username)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)
