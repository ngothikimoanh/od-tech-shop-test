from configparser import SectionProxy

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from models.user import User


class LoginPage(BasePage):

    phone_number_input = ("id", "phone_number")
    password_input = ("id", "password")
    login_button = ("id", "login_submit_btn")

    def enter_phone_number(self, phone_number):
        self.send_keys(self.phone_number_input, phone_number)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def get_user_by_phone_number_from_db(self, phone_number: str):
        return self.db.query(User).filter(User.phone_number == phone_number).first()
