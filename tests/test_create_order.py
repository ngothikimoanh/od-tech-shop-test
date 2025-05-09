from pages.create_order_page import CreateOrderPage
from pages.home_page import HomePage
from pages.login_page import LoginPage, ProfilePage
from pages.product_detail_page import ProductDetailPage


def test_add_one_product_to_cart(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

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


def test_add_multiple_products_to_cart(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

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


def test_add_many_quantity_product_to_cart(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

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


def test_buy_now_btn_in_home_page(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)

    first_product = home_page.get_first_product()
    product_name = home_page.get_product_name(first_product)
    home_page.click_buy_now_btn(first_product)

    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_cart_by_browser_id()


def test_buy_now_in_detail_page(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)
    home_page.click_first_product()

    product_detail_page = ProductDetailPage(driver, config)

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert product_name != '' and product_name is not None

    product_detail_page.click_buy_now_btn()
    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.clear_cart_by_browser_id()


def test_add_one_product_to_car_logged_in(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

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

    create_order_page = CreateOrderPage(driver, config, db=database)
    user_name = create_order_page.get_buyer_name()
    user_phone_number = create_order_page.get_buyer_phone_number()
    user_address = create_order_page.get_buyer_address()

    assert user_name in driver.page_source
    assert user_phone_number in driver.page_source
    assert user_address in driver.page_source
    assert product_name in driver.page_source

    create_order_page.clear_carts(phone_number=config["buyer_phone_number"])


def test_sync_updated_user_name_to_cart_logged_in(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

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
    create_order_page.click_profile_btn()

    login_page = ProfilePage(driver, config)
    login_page.enter_user_name("kim oanh")
    login_page.click_update_btn()
    assert "Cập nhật thông tin thành công" in driver.page_source

    user_name = login_page.get_user_name()
    login_page.click_cart_btn()
    assert user_name in driver.page_source

    create_order_page.clear_carts(phone_number=config["buyer_phone_number"])


def test_sync_updated_user_address_to_cart_logged_in(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

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
    create_order_page.click_profile_btn()

    login_page = ProfilePage(driver, config)
    login_page.enter_user_address("Quảng Nam")
    login_page.click_update_btn()
    assert "Cập nhật thông tin thành công" in driver.page_source

    user_address = login_page.get_user_address()
    login_page.click_cart_btn()
    assert user_address in driver.page_source

    create_order_page.clear_carts(phone_number=config["buyer_phone_number"])


def test_sync_updated_user_infor_to_cart_logged_in(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

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
    create_order_page.click_profile_btn()

    login_page = ProfilePage(driver, config)
    login_page.enter_user_name("oanh")
    login_page.enter_user_address("Đà Nẵng")
    login_page.click_update_btn()
    assert "Cập nhật thông tin thành công" in driver.page_source

    user_name = login_page.get_user_name()
    user_address = login_page.get_user_address()
    login_page.click_cart_btn()
    assert user_name in driver.page_source
    assert user_address in driver.page_source

    create_order_page.clear_carts(phone_number=config["buyer_phone_number"])


def test_delete_product_cart(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)
    home_page.click_first_product()

    product_detail_page = ProductDetailPage(driver, config)
    product_detail_page.click_add_to_cart_btn()

    product_name = product_detail_page.get_product_name_title().replace("Điện thoại ", "")
    assert product_name != '' and product_name is not None

    product_detail_page.click_cart_btn()
    assert product_name in driver.page_source

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.click_minus_quantity()
    assert "Giỏ hàng trống" in driver.page_source


def test_order_fails_when_quantity_exceeds_available_stock(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)
    product_name = home_page.get_product_name(home_page.get_first_product())
    home_page.click_buy_now_btn(home_page.get_first_product())
    create_order_page = CreateOrderPage(driver, config, db=database)
    quantity_number_increase = 6
    for _ in range(quantity_number_increase):
        create_order_page.click_plus_quantity()

    create_order_page.enter_buyer_name(config['buyer_name'])
    create_order_page.enter_buyer_phone_number(config['buyer_phone_number'])
    create_order_page.enter_buyer_address(config['buyer_address'])
    create_order_page.click_banking_payment_btn()
    create_order_page.click_order_btn()

    assert f"Sản phẩm <strong>{product_name}</strong> không đủ số lượng" in driver.page_source


def test_order_fails_with_only_user_name_provided(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()
    phone_number = "0784253462"
    password = "Kimoanh@2003"
    name = "kim oanh"

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(phone_number)
    login_page.enter_password(password)
    login_page.click_login()

    home_page.click_buy_now_btn(home_page.get_first_product())
    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.enter_buyer_phone_number("")
    create_order_page.enter_buyer_name(name)
    create_order_page.click_order_btn()

    assert "Đặt hàng thất bại" in driver.page_source
    name = ""
    create_order_page.clear_carts(phone_number=phone_number)


def test_order_fails_with_user_phone_number_provided(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()
    phone_number = "0784253462"
    password = "Kimoanh@2003"

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(phone_number)
    login_page.enter_password(password)
    login_page.click_login()

    home_page.click_buy_now_btn(home_page.get_first_product())
    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.click_order_btn()

    assert "Đặt hàng thất bại" in driver.page_source
    create_order_page.clear_carts(phone_number=phone_number)


def test_order_fails_with_user_address_provided(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()
    phone_number = "0784253462"
    password = "Kimoanh@2003"
    address = "Đà Nẵng"

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(phone_number)
    login_page.enter_password(password)
    login_page.click_login()

    home_page.click_buy_now_btn(home_page.get_first_product())
    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.enter_buyer_address(address)
    create_order_page.click_order_btn()

    assert "Đặt hàng thất bại" in driver.page_source
    address = ""
    create_order_page.clear_carts(phone_number=phone_number)


def test_order_with_cash_payment(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)

    home_page.click_buy_now_btn(home_page.get_first_product())

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.enter_buyer_name(config['buyer_name'])
    create_order_page.enter_buyer_phone_number(config['buyer_phone_number'])
    create_order_page.enter_buyer_address(config['buyer_address'])
    create_order_page.click_cash_payment_btn()
    create_order_page.click_order_btn()

    orders = create_order_page.get_order_in_db()
    assert len(orders) > 0
    create_order_page.clear_order(phone_number=config['buyer_phone_number'])


def test_order_with_banking_payment(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)

    home_page.click_buy_now_btn(home_page.get_first_product())

    create_order_page = CreateOrderPage(driver, config, db=database)
    create_order_page.enter_buyer_name(config['buyer_name'])
    create_order_page.enter_buyer_phone_number(config['buyer_phone_number'])
    create_order_page.enter_buyer_address(config['buyer_address'])
    create_order_page.click_banking_payment_btn()
    create_order_page.click_order_btn()

    orders = create_order_page.get_order_in_db()
    assert len(orders) > 0
    create_order_page.clear_order(phone_number=config['buyer_phone_number'])


def test_order_with_logged_in(driver, config, database):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)

    home_page.click_login_btn()
    login_page = LoginPage(driver, config)
    login_page.enter_phone_number(config['buyer_phone_number'])
    login_page.enter_password(config['buyer_password'])
    login_page.click_login()

    home_page.click_buy_now_btn(home_page.get_first_product())

    create_order_page = CreateOrderPage(driver, config, db=database)
    user_name = create_order_page.get_buyer_name()
    user_phone_number = create_order_page.get_buyer_phone_number()
    user_address = create_order_page.get_buyer_address()

    assert user_name in driver.page_source
    assert user_phone_number in driver.page_source
    assert user_address in driver.page_source

    create_order_page.click_order_btn()

    orders = create_order_page.get_order_in_db()
    assert len(orders) > 0
    create_order_page.clear_order(phone_number=config['buyer_phone_number'])
