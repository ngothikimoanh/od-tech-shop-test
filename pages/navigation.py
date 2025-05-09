import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Navigation(BasePage):
    logo_btn = (By.ID, "navBrand")
    cart_btn = (By.ID, "navCartBtn")
    login_btn = (By.ID, "navLoginBtn")
    profile_btn = (By.ID, "navprofileBtn")
    admin_btn = (By.ID, "navAdminBtn")
    admin_order_btn = (By.ID, "navAdminOrders")

    def click_logo_btn(self):
        self.click(self.logo_btn)
        time.sleep(3)

    def click_cart_btn(self):
        self.click(self.cart_btn)
        time.sleep(3)

    def click_login_btn(self):
        self.click(self.login_btn)
        time.sleep(3)

    def click_profile_btn(self):
        self.click(self.profile_btn)
        time.sleep(3)

    def click_admin_btn(self):
        self.click(self.admin_btn)
        time.sleep(3)

    def click_admin_order_btn(self):
        self.click(self.admin_order_btn)
        time.sleep(3)
