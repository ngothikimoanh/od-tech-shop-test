from pages.base_page import BasePage


class LoginPage(BasePage):
    phone_number_input = ("id", "loginPhoneNumberInput")
    password_input = ("id", "loginPasswordInput")
    login_button = ("id", "loginSubmitBtn")

    def enter_phone_number(self, phone_number):
        self.send_keys(self.phone_number_input, phone_number)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)
