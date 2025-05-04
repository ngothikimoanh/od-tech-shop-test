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
    home_page.click_first_product()

    product_detail_page = ProductDetailPage(driver, config)

    number_add_to_cart = 5
    for _ in range(number_add_to_cart):
        product_detail_page.click_add_to_cart_btn()

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert product_name != '' and product_name is not None

    product_detail_page.click_cart_btn()
    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    assert create_order_page.get_number_product_in_cart_text() == number_add_to_cart

    create_order_page.clear_cart_by_browser_id()


def test_add_multiple_products_to_cart_not_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_first_product()

    product_detail_page = ProductDetailPage(driver, config)
    product_detail_page.click_add_to_cart_btn()

    first_product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert first_product_name != '' and first_product_name is not None

    product_detail_page.click_logo_btn()
    home_page.click_second_product()
    product_detail_page.click_add_to_cart_btn()

    second_product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert second_product_name != '' and second_product_name is not None

    product_detail_page.click_cart_btn()
    assert first_product_name in driver.page_source
    assert second_product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_cart_by_browser_id()


def test_buy_now_btn_in_home_page_not_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)

    first_product = home_page.get_first_product()
    product_name = home_page.get_product_name(first_product)
    home_page.click_buy_now_btn(first_product)

    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_cart_by_browser_id()


def test_buy_now_in_detail_page_not_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_first_product()

    product_detail_page = ProductDetailPage(driver, config)

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert product_name != '' and product_name is not None

    product_detail_page.click_buy_now_btn()
    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_cart_by_browser_id()


def test_add_one_product_to_cart_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config['buyer_phone_number'])
    login_page.enter_password(config['buyer_password'])
    login_page.click_login()

    home_page.click_first_product()

    product_detail_page = ProductDetailPage(driver, config)
    product_detail_page.click_add_to_cart_btn()

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert product_name != '' and product_name is not None

    product_detail_page.click_cart_btn()
    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_carts()


def test_add_many_quantity_product_to_cart_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config['buyer_phone_number'])
    login_page.enter_password(config['buyer_password'])
    login_page.click_login()

    home_page.click_first_product()

    product_detail_page = ProductDetailPage(driver, config)

    number_add_to_cart = 5
    for _ in range(number_add_to_cart):
        product_detail_page.click_add_to_cart_btn()

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert product_name != '' and product_name is not None

    product_detail_page.click_cart_btn()
    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    assert create_order_page.get_number_product_in_cart_text() == number_add_to_cart

    create_order_page.clear_carts()


def test_add_multiple_products_to_cart_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config['buyer_phone_number'])
    login_page.enter_password(config['buyer_password'])
    login_page.click_login()

    home_page.click_first_product()

    product_detail_page = ProductDetailPage(driver, config)
    product_detail_page.click_add_to_cart_btn()

    first_product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert first_product_name != '' and first_product_name is not None

    product_detail_page.click_logo_btn()
    home_page.click_second_product()
    product_detail_page.click_add_to_cart_btn()

    second_product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert second_product_name != '' and second_product_name is not None

    product_detail_page.click_cart_btn()
    assert first_product_name in driver.page_source
    assert second_product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_carts()


def test_buy_now_btn_in_home_page_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config['buyer_phone_number'])
    login_page.enter_password(config['buyer_password'])
    login_page.click_login()

    first_product = home_page.get_first_product()
    product_name = home_page.get_product_name(first_product)
    home_page.click_buy_now_btn(first_product)

    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_carts()


def test_buy_now_in_detail_page_logged_in(driver, config, database):
    driver.get(config["base_url"])

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config['buyer_phone_number'])
    login_page.enter_password(config['buyer_password'])
    login_page.click_login()

    home_page.click_first_product()

    product_detail_page = ProductDetailPage(driver, config)

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert product_name != '' and product_name is not None

    product_detail_page.click_buy_now_btn()
    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_carts()
