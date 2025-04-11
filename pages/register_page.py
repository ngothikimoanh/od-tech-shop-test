from selenium.webdriver.common.by import By
from sqlalchemy.orm import Session

from models.user import User
from pages.base_page import BasePage


class RegisterPage(BasePage):
    URL = "auth/register"

    phone_number_input = (By.ID, "phone_number")
    password_input = (By.ID, "password")
    confirm_password_input = (By.ID, "password_confirm")
    register_button = (By.ID, "register_submit_btn")

    def __init__(self, driver, config, db: Session | None = None, timeout=10):
        super().__init__(driver, config, db, timeout)

        driver.get(self.config['base_url'] + self.URL)

    def enter_phone_number(self, phone_number):
        self.send_keys(self.phone_number_input, phone_number)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def enter_confirm_password(self, confirm_password):
        self.send_keys(self.confirm_password_input, confirm_password)

    def click_register(self):
        self.click(self.register_button)

    def get_user_by_phone_number_from_db(self, phone_number: str):
        return self.db.query(User).filter(User.phone_number == phone_number).first()

    def delete_user_by_phone_number_in_db(self, phone_number: str):
        user = self.get_user_by_phone_number_from_db(phone_number)
        self.db.delete(user)
        self.db.commit()
