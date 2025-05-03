from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Navigation(BasePage):
    cart_btn = (By.ID, "cart")
    login_btn = (By.ID, "nav_login_btn")

    def click_cart_btn(self):
        self.click(self.cart_btn)

    def click_login_btn(self):
        self.click(self.login_btn)