from selenium.webdriver.common.by import By

from pages.navigation import Navigation

class ProductDetailPage(Navigation):
    product_name_title = (By.ID, "product_name_title")

    add_to_cart_btn = (By.ID, "add_cart")
    buy_now_btn = (By.ID, "buy_now")

    def click_add_to_cart_btn(self):
        self.click(self.add_to_cart_btn)

    def click_buy_now_btn(self):
        self.click(self.buy_now_btn)

    def get_product_name_title(self):
        return self.get_text(self.product_name_title)
