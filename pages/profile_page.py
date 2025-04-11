from configparser import SectionProxy

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from sqlalchemy.orm import Session

from pages.base_page import BasePage
from models.user import User


class ProfilePage(BasePage):
    URL = "users/profile"

    phone_number = (By.ID, "phone_number_input")
    email = (By.ID, "email_input")
    last_name = (By.ID, "last_name_input")
    first_name = (By.ID, "first_name_input")
    update_button = (By.ID, "update_profile_btn")
    points = (By.ID, "user_points")

    def __init__(self, driver: WebDriver, config: SectionProxy, db: Session | None = None, timeout: int = 10):
        super().__init__(driver, config, db, timeout)
        super().set_session_id()
        driver.get(self.config['base_url'] + self.URL)

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

    def get_points(self):
        return self.get_text(self.points)

    def get_points_from_db(self):
        point = self.db.query(User).filter(User.phone_number == self.config['phone_number']).first().points
        return f"{point:0.0f}"
