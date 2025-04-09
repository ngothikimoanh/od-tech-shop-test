from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfilePage(BasePage):
    phone_number_input = (By.NAME, "phone_number")
    email = (By.NAME, "email")
    last_name_input = (By.NAME, "last_name")
    first_name_input = (By.NAME, "first_name")
    update_button = (By.ID, "update_profile_btn")
    change_password = (By.CSS_SELECTOR, ".fa-solid.fa-key")

    success_message = (By.CSS_SELECTOR, ".toast-header.bg-primary.text-white")
    error_message = (By.CLASS_NAME, "alert-danger")

    def enter_phone_number(self, phone_number):
        self.send_keys(self.phone_number_input, phone_number)

    def enter_email(self, email):
        self.send_keys(self.email, email)

    def enter_last_name(self, last_name):
        self.send_keys(self.last_name_input, last_name)

    def enter_first_name(self, first_name):
        self.send_keys(self.first_name_input, first_name)

    def click_update(self):
        self.click(self.update_button)

    def click_change_password(self):
        self.click(self.change_password)
