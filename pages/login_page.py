import time

from selenium.webdriver.common.by import By
from sqlalchemy import text

from pages.base_page import BasePage
from pages.navigation import Navigation


class LoginPage(BasePage):
    phone_number_input = (By.ID, "loginPhoneNumberInput")
    password_input = (By.ID, "loginPasswordInput")
    login_button = (By.ID, "loginSubmitBtn")
    register_link = (By.ID, "registerLink")

    def enter_phone_number(self, phone_number):
        self.send_keys(self.phone_number_input, phone_number)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)
        time.sleep(3)

    def get_user_by_phone_number_from_db(self, phone_number):
        return self.db.execute(
            text("SELECT * FROM users WHERE phone_number = :phone_number"), {"phone_number": phone_number}
        ).fetchone()

    def click_register_link(self):
        self.click(self.register_link)


class ProfilePage(Navigation):
    user_name = (By.ID, "name")
    user_phone_number = (By.ID, "phoneNumber")
    user_birthday = (By.ID, "birthday")
    user_email = (By.ID, "email")
    user_address = (By.ID, "address")
    update_btn = (By.ID, "updateBtn")

    def enter_user_name(self, name):
        self.send_keys(self.user_name, name)

    def enter_user_phone_number(self, phone_number):
        self.send_keys(self.user_phone_number, phone_number)

    def enter_user_birthday(self, birthday):
        self.send_keys(self.user_birthday, birthday)

    def enter_user_email(self, email):
        self.send_keys(self.user_email, email)

    def enter_user_address(self, address):
        self.send_keys(self.user_address, address)

    def click_update_btn(self):
        self.click(self.update_btn)

    def get_user_name(self):
        return self.get_text(self.user_name)

    def get_user_address(self):
        return self.get_text(self.user_address)
