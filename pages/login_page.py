from configparser import SectionProxy

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from sqlalchemy.orm import Session

from pages.base_page import BasePage
from models.user import User


class LoginPage(BasePage):
    URL = "login"

    phone_number_input = (By.ID, "phone_number")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login_submit_btn")

    def __init__(self, driver: WebDriver, config: SectionProxy, db: Session | None = None, timeout: int = 10):
        super().__init__(driver=driver, config=config, db=db, timeout=timeout)
        driver.get(self.config['base_url'] + self.URL)

    def enter_phone_number(self, phone_number):
        self.send_keys(self.phone_number_input, phone_number)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def get_user_by_phone_number_from_db(self, phone_number: str):
        return self.db.query(User).filter(User.phone_number == phone_number).first()

