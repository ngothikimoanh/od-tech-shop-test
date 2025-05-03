from pages.navigation import Navigation
from selenium.webdriver.common.by import By


class HomePage(Navigation):

    product_name = (By.CLASS_NAME, "card-title")
    buy_now_btn = (By.ID, "buy_now")

    def get_product_name(self, index=0):
        elements = self.find_elements(self.product_name)
        if index < len(elements):
            return elements[index].text

    def click_product_name(self, index=0):
        elements = self.find_elements(self.product_name)
        if index < len(elements):
            elements[index].click()

    def click_buy_now_btn(self, index=0):
        self.click(self.buy_now_btn)