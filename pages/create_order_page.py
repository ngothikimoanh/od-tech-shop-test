import time

from selenium.webdriver.common.by import By
from pages.navigation import Navigation
from sqlalchemy import text
import re


class CreateOrderPage(Navigation):
    minus_quantity = (By.ID, "minus_quantity")
    plus_quantity = (By.ID, "plus_quantity")

    buyer_name_input = (By.ID, "orderBuyerName")
    buyer_phone_number_input = (By.ID, "orderBuyerPhoneNumber")
    buyer_address_input = (By.ID, "orderBuyerAddress")

    use_points = (By.ID, "isUsePoint")
    order_accumulated_points = (By.ID, "order_accumulated_points")

    cash_payment_btn = (By.ID, "cashOnDelivered")
    banking_payment_btn = (By.ID, "transferNow")

    order_btn = (By.ID, "orderBtn")
    order_temporary_total = (By.ID, "order_temporary_total")
    order_total_amount = (By.ID, "orderTotalAmount")

    number_product_in_cart = (By.CSS_SELECTOR, '.input-group-text.px-3')

    def click_minus_quantity(self):
        self.click(self.minus_quantity)

    def click_plus_quantity(self):
        self.click(self.plus_quantity)

    def enter_buyer_name(self, order_buyer_name):
        self.send_keys(self.buyer_name_input, order_buyer_name)

    def enter_buyer_phone_number(self, order_buyer_phone_number):
        self.send_keys(self.buyer_phone_number_input, order_buyer_phone_number)

    def enter_buyer_address(self, order_buyer_address):
        self.send_keys(self.buyer_address_input, order_buyer_address)

    def click_use_points(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            self.click(self.use_points)
        except:
            pass

    def click_cash_payment_btn(self):
        self.click(self.cash_payment_btn)

    def click_banking_payment_btn(self):
        self.click(self.banking_payment_btn)

    def click_order_btn(self):
        self.click(self.order_btn)
        time.sleep(3)

    def clear_carts(self):
        self.db.execute(text(
            f"DELETE FROM carts WHERE user_id = (SELECT id FROM users WHERE phone_number=:phone_number)"),
            {"phone_number": self.config["buyer_phone_number"]})
        self.db.commit()

    def get_browser_id(self):
        return self.driver.get_cookie("browser_id")["value"]

    def clear_cart_by_browser_id(self):
        browser_id = self.get_browser_id()
        self.db.execute(text("DELETE FROM carts WHERE browser_id = :browser_id"), {"browser_id": browser_id})
        self.db.commit()

    def get_total_money(self):
        total_money = self.get_text(self.order_total_amount)
        return int(total_money.replace(".", "").replace("₫", "").strip())

    def get_temporary_total(self):
        temp_total = self.get_text(self.order_temporary_total)
        return int(temp_total.replace(".", "").replace("₫", "").strip())

    def get_accumulated_points(self):
        try:
            accumulated_points = self.get_text(self.order_accumulated_points)
            cleaned = re.sub(r"[^\d-]", "", accumulated_points)
            return int(cleaned) if cleaned else 0
        except:
            return 0

    def get_number_product_in_cart_text(self):
        return int(self.get_text(self.number_product_in_cart))

    def get_order_in_db(self):
        return self.db.execute(
            text(
                "SELECT id FROM orders WHERE buyer_phone_number = :buyer_phone_number and address = :buyer_address and buyer_name = :buyer_name and time_cancel is null"
            ),
            {'buyer_phone_number': self.config["buyer_phone_number"],
             'buyer_address': self.config["buyer_address"],
             'buyer_name': self.config["buyer_name"]}
        ).fetchall()
