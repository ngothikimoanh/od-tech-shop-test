import time

from selenium.webdriver.remote.webelement import WebElement

from pages.navigation import Navigation
from selenium.webdriver.common.by import By


class HomePage(Navigation):
    product_list = (By.ID, "productsContainer")
    buy_now_button = (By.CSS_SELECTOR, '.btn.btn-outline-primary')
    product_name = (By.CSS_SELECTOR, ".card-title.text-truncate")

    def get_products(self):
        return self.find_element(self.product_list)

    def get_first_product(self):
        return self.get_products().find_element("xpath", "./*")

    def click_first_product(self):
        self.get_first_product().click()
        time.sleep(3)

    def click_buy_now_btn(self, product_element: WebElement):
        product_element.find_element(*self.buy_now_button).click()
        time.sleep(3)

    def get_product_name(self, product_element: WebElement):
        return product_element.find_element(*self.product_name).text

    def get_second_product(self):
        return self.get_products().find_element("xpath", "./*[2]")

    def click_second_product(self):
        self.get_second_product().click()
        time.sleep(3)
