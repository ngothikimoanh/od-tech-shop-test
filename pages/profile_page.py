from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfilePage(BasePage):
    phone_number = (By.ID, "phone_number_input")
    email = (By.ID, "email_input")
    last_name = (By.ID, "last_name_input")
    first_name = (By.ID, "first_name_input")
    update_button = (By.ID, "update_profile_btn")

    def enter_phone_number(self, phone_number):
        self.send_keys(self.phone_number, phone_number)

    def enter_email(self, email_input):
        self.send_keys(self.email, email_input)

    def enter_last_name(self, last_name_input):
        self.send_keys(self.last_name, last_name_input)

    def enter_first_name(self, first_name_input):
        self.send_keys(self.first_name, first_name_input)

    def click_update(self):
        self.click(self.update_button)
