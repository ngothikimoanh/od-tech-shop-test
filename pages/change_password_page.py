from configparser import SectionProxy

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from sqlalchemy.orm import Session

from models.django_session import DjangoSession
from models.user import User

from pages.base_page import BasePage


class ChangePasswordPage(BasePage):
    URL = "users/change_password"

    old_password_input = (By.ID, "old_password")
    new_password_input = (By.ID, "new_password")
    confirm_new_password_input = (By.ID, "new_password_again")
    change_password_button = (By.ID, "change_password_btn")

    def __init__(self, driver: WebDriver, config: SectionProxy, db: Session | None = None, timeout: int = 10):
        super().__init__(driver, config, db, timeout)
        super().set_session_id()
        driver.get(self.config['base_url'] + self.URL)

    def enter_old_password(self, old_password):
        self.send_keys(self.old_password_input, old_password)

    def enter_new_password(self, new_password):
        self.send_keys(self.new_password_input, new_password)

    def enter_new_password_again(self, new_password_again):
        self.send_keys(self.confirm_new_password_input, new_password_again)

    def click_change_password(self):
        self.click(self.change_password_button)

    def get_password(self):
        return self.db.query(User).filter(User.phone_number == self.config['phone_number']).first().password

    def set_password(self, password: str):
        self.db.query(User).filter(User.phone_number == self.config['phone_number']).update({User.password: password})
        self.db.commit()

    def get_django_session(self) -> dict:
        data = self.db.query(DjangoSession).filter(DjangoSession.session_key == self.get_session_id()).first().__dict__
        del data['_sa_instance_state']
        return data

    def set_django_session(self, data: dict):
        django_session = DjangoSession(**data)
        self.db.add(django_session)
        self.db.commit()
