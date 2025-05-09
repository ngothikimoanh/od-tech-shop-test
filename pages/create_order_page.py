import re
import time
from tkinter import SE

from selenium.webdriver.common.by import By
from sqlalchemy import text

from pages.navigation import Navigation


class CreateOrderPage(Navigation):
    minus_quantity = (By.ID, "minusBtn")
    plus_quantity = (By.ID, "plusBtn")

    buyer_name_input = (By.ID, "orderBuyerName")
    buyer_phone_number_input = (By.ID, "orderBuyerPhoneNumber")
    buyer_address_input = (By.ID, "orderBuyerAddress")

    use_points = (By.ID, "isUsePoint")
    order_accumulated_points = (By.ID, "orderPoint")

    cash_payment_btn = (By.ID, "cashOnDelivered")
    banking_payment_btn = (By.ID, "transferNow")

    order_btn = (By.ID, "orderBtn")
    order_temporary_total = (By.ID, "orderTemporary")
    order_total_amount = (By.ID, "orderTotalAmount")

    number_product_in_cart = (By.CSS_SELECTOR, '.input-group-text.px-3')

    def click_minus_quantity(self):
        self.click(self.minus_quantity)
        time.sleep(3)

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
        time.sleep(3)

    def click_banking_payment_btn(self):
        self.click(self.banking_payment_btn)
        time.sleep(3)

    def click_order_btn(self):
        self.click(self.order_btn)
        time.sleep(3)

    def clear_carts(self, phone_number):
        self.db.execute(text(
            f"DELETE FROM carts WHERE user_id = (SELECT id FROM users WHERE phone_number=:phone_number)"),
            {"phone_number": phone_number})
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

    def get_buyer_name(self):
        return self.get_text(self.buyer_name_input)

    def get_buyer_phone_number(self):
        return self.get_text(self.buyer_phone_number_input)

    def get_buyer_address(self):
        return self.get_text(self.buyer_address_input)

    def clear_order(self, phone_number):
        order = self.db.execute(
            text('select id, point_used from orders where buyer_phone_number = :phone_number order by time_order desc limit 1'),
            {'phone_number': phone_number}
        ).fetchall()
        if order:
            order_id = order[0][0]
            point_used = order[0][1]

            self.db.execute(text("update devices set status = 'Có sẵn' where id in (select device_id from order_devices where order_id = :order_id)"),
                            {'order_id': order_id})
            self.db.execute(text('delete from order_devices where order_id = :order_id'), {'order_id': order_id})

            self.db.execute(text('delete from order_products where order_id = :order_id'), {'order_id': order_id})
            self.db.execute(
                text('update users set points = points + :point_used where phone_number = :phone_number'),
                {'point_used': point_used, 'phone_number': phone_number}
            )
            self.db.execute(text('delete from orders where id = :order_id'), {'order_id': order_id})
            self.db.commit()
