from pages.navigation import Navigation
from selenium.webdriver.common.by import By

class HomePage(Navigation):
    product_list = (By.ID, "productsContainer")

    def get_products(self):
        return self.find_element(self.product_list)

    def get_first_product(self):
        return self.get_products().find_element("xpath", "./*")

    def click_first_product(self):
        self.get_first_product().click()

