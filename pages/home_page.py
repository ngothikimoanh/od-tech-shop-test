from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.navigation import Navigation


class HomePage(Navigation):

    product_name = (By.ID, "product_name")
    buy_now_btn = (By.ID, "buy_now")

    def click_product_name(self):
        self.click(self.product_name)

    def click_buy_now_btn(self):
        self.click(self.buy_now_btn)