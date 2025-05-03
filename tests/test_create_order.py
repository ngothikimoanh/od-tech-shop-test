from pages import home_page
from pages.create_order_page import CreatOrderPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_detail_page import ProductDetailPage


def test_add_one_product_to_cart_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config["buyer_phone_number"])
    login_page.enter_password(config["buyer_password"])
    login_page.click_login()

    home_page.click_product_name(index=0)
    product_detail_page = ProductDetailPage(driver, config)
    product_detail_page.click_add_to_cart_btn()

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    print(f"Product name: {product_name}")
    product_detail_page.click_cart_btn()
    assert product_name in driver.page_source

    create_order_page = CreatOrderPage(driver, config, db=database)
    create_order_page.clear_carts()

def test_add_many_quantity_product_to_cart_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config["buyer_phone_number"])
    login_page.enter_password(config["buyer_password"])
    login_page.click_login()

    home_page.click_product_name(index=0)
    product_detail_page = ProductDetailPage(driver, config)
    for _ in range(4):
        product_detail_page.click_add_to_cart_btn()

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    print(f"Product name: {product_name}")
    product_detail_page.click_cart_btn()
    assert product_name in driver.page_source

    create_order_page = CreatOrderPage(driver, config, db=database)
    create_order_page.clear_carts()

def test_add_multiple_products_to_cart_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config["buyer_phone_number"])
    login_page.enter_password(config["buyer_password"])
    login_page.click_login()

    product_names = []

    for index in range(3):
        home_page.click_product_name(index=index)
        product_detail_page = ProductDetailPage(driver, config)
        product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
        product_names.append(product_name)

        product_detail_page.click_add_to_cart_btn()
        product_detail_page.click_logo_btn()

    print(f"Product name: {product_names}")
    for name in product_names:
        assert name in driver.page_source, f"{name} not found in cart page"
    create_order_page = CreatOrderPage(driver, config, db=database)
    create_order_page.clear_carts()

def test_buy_now_btn_in_home_page_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config["buyer_phone_number"])
    login_page.enter_password(config["buyer_password"])
    login_page.click_login()

    product_name = home_page.get_product_name(index=0)
    home_page.click_buy_now_btn()

    assert product_name in driver.page_source
    create_order_page = CreatOrderPage(driver, config, db=database)
    create_order_page.clear_carts()

