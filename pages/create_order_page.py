from selenium.webdriver.common.by import By
from pages.navigation import Navigation
from sqlalchemy import text


class CreatOrderPage(Navigation):
    minus_quantity = (By.ID, "minus_quantity")
    plus_quantity = (By.ID, "plus_quantity")

    buyer_name_input = (By.ID, "orderBuyerName")
    buyer_phone_number_input = (By.ID, "orderBuyerPhoneNumber")
    buyer_address_input = (By.ID, "orderBuyerAddress")

    use_points = (By.ID, "isUsePoint")

    cash_payment_btn = (By.ID, "cashOnDelivered")
    banking_payment_btn = (By.ID, "transferNow")

    order_btn = (By.ID, "order")

    def click_minus_quantity(self):
        self.click(self.minus_quantity)

    def click_plus_quantity(self):
        self.click(self.plus_quantity)

    def enter_buyer_name(self, orderBuyerName):
        self.send_keys(self.buyer_name_input, orderBuyerName)

    def enter_buyer_phone_number(self, orderBuyerPhoneNumber):
        self.send_keys(self.buyer_phone_number_input, orderBuyerPhoneNumber)

    def enter_buyer_address(self, orderBuyerAddress):
        self.send_keys(self.buyer_address_input, orderBuyerAddress)

    def click_use_points(self):
        self.click(self.use_points)

    def click_cash_payment_btn(self):
        self.click(self.cash_payment_btn)

    def click_banking_payment_btn(self):
        self.click(self.banking_payment_btn)

    def click_order_btn(self):
        self.click(self.order_btn)

    def clear_carts(self):
        self.db.execute(text(
            f"DELETE FROM carts WHERE user_id = (SELECT id FROM users WHERE phone_number=:phone_number)"),
            {"phone_number" : self.config["buyer_phone_number"]})
        self.db.commit()
