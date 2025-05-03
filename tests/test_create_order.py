from pages.create_order_page import CreatOrderPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_detail_page import ProductDetailPage


def test_add_product_to_cart(driver, config, database):
    driver.maximize_window()
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config["buyer_phone_number"])
    login_page.enter_password(config["buyer_password"])
    login_page.click_login()

    home_page.click_product_name()
    product_detail_page = ProductDetailPage(driver, config)
    product_detail_page.click_add_to_cart_btn()

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    print(f"Product name: {product_name}")
    product_detail_page.click_cart_btn()
    assert product_name in driver.page_source

    create_order_page = CreatOrderPage(driver, config,  db=database)
    create_order_page.clear_carts()









