from pages.base_page import BasePage


class Navigation(BasePage):
    logo_btn =  ("id", "logo")

    cart_btn = ("id", "cart")
    login_btn = ("id", "nav_login_btn")

    def click_logo_btn(self):
        self.click(self.logo_btn)

    def click_cart_btn(self):
        self.click(self.cart_btn)

    def click_login_btn(self):
        self.click(self.login_btn)