from selenium.webdriver.common.by import By

from pages.navigation import Navigation

import time


class ProductDetailPage(Navigation):
    product_name_title = (By.ID, "productNameTitle")

    add_to_cart_btn = (By.ID, "addToCartBtn")
    buy_now_btn = (By.ID, "buyNowBtn")

    def click_add_to_cart_btn(self):
        self.click(self.add_to_cart_btn)
        time.sleep(3)

    def click_buy_now_btn(self):
        self.click(self.buy_now_btn)

    def get_product_name_title(self):
        return self.get_text(self.product_name_title)
