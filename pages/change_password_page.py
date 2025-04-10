from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ChangePasswordPage(BasePage):
    old_password_input = (By.ID, "old_password")
    new_password_input = (By.ID, "new_password")
    confirm_new_password_input = (By.ID, "new_password_again")
    change_password_button = (By.ID, "change_password_btn")

    def __init__(self, driver, config, timeout=10):
        super().__init__(driver, config, timeout)
        print('config= ',config)

        base_url = config.get("base_url", "http://localhost:8000/")
        driver.get(base_url)
        driver.add_cookie(cookie_dict={
            'name': 'sessionid',
            'value': config['sessionid'],
        })

        driver.get(base_url + "users/change_password")

    def enter_old_password(self, old_password):
        self.send_keys(self.old_password_input, old_password)

    def enter_new_password(self, new_password):
        self.send_keys(self.new_password_input, new_password)

    def enter_new_password_again(self, new_password_again):
        self.send_keys(self.confirm_new_password_input, new_password_again)

    def click_change_password(self):
        self.click(self.change_password_button)
