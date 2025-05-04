from pages.create_order_page import CreateOrderPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_detail_page import ProductDetailPage


def test_add_one_product_to_cart_not_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_first_product()

    product_detail_page = ProductDetailPage(driver, config)
    product_detail_page.click_add_to_cart_btn()

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert product_name != '' and product_name is not None

    product_detail_page.click_cart_btn()
    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_cart_by_browser_id()


def test_add_many_quantity_product_to_cart_not_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_product_name(index=0)
    product_detail_page = ProductDetailPage(driver, config)
    for _ in range(4):
        product_detail_page.click_add_to_cart_btn()

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    print(f"Product name: {product_name}")
    product_detail_page.click_cart_btn()
    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_carts()


def test_add_multiple_products_to_cart_not_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
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
    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_carts()


def test_buy_now_btn_in_home_page_not_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    product = home_page.get_first_product()
    home_page.click_buy_now_btn()
    assert product_name in driver.page_source
    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_carts()


def test_buy_now_in_detail_page_not_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_product_name(index=0)
    product_detail_page = ProductDetailPage(driver, config)
    product_detail_page.click_buy_now_btn()
    assert product_detail_page.get_product_name_title() in driver.page_source


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

    create_order_page = CreateOrderPage(driver, config, db=database)
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

    create_order_page = CreateOrderPage(driver, config, db=database)
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
    create_order_page = CreateOrderPage(driver, config, db=database)
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
    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_carts()


def test_creat_order_with_use_points_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config["buyer_phone_number"])
    login_page.enter_password(config["buyer_password"])
    login_page.click_login()

    home_page.click_buy_now_btn(index=0)
    create_order_page = CreateOrderPage(driver, config, db=database)

    create_order_page.click_use_points()
    total_amount = create_order_page.get_total_money()
    temporary_total = create_order_page.get_temporary_total()
    accumulated_points = create_order_page.get_accumulated_points()

    total_amount = temporary_total + accumulated_points
    print(f"Total amount: {total_amount}", create_order_page.get_total_money())

    assert total_amount == create_order_page.get_total_money(), f"Tổng tiền ({total_amount}) != Tạm tính ({temporary_total}) - Điểm ({accumulated_points})"
    create_order_page.clear_carts()


def test_creat_order_with_use_points_and_cash_payment_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config["buyer_phone_number"])
    login_page.enter_password(config["buyer_password"])
    login_page.click_login()

    home_page.click_buy_now_btn(index=0)
    create_order_page = CreateOrderPage(driver, config, db=database)

    create_order_page.click_use_points()
    total_amount = create_order_page.get_total_money()
    temporary_total = create_order_page.get_temporary_total()
    accumulated_points = create_order_page.get_accumulated_points()

    total_amount = temporary_total + accumulated_points
    print(f"Total amount: {total_amount}", create_order_page.get_total_money())

    assert total_amount == create_order_page.get_total_money(), f"Tổng tiền ({total_amount}) != Tạm tính ({temporary_total}) - Điểm ({accumulated_points})"

    create_order_page.click_cash_payment_btn()
    create_order_page.click_order_btn()

    assert create_order_page.has_order_with_phone(database, config["buyer_phone_number"]), \
        f"Không tìm thấy đơn hàng với số điện thoại {config['buyer_phone_number']}"
