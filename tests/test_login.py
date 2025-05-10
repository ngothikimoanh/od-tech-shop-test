
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_missing_phone_number(driver, config):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)

    login_page.enter_phone_number("")
    login_page.enter_password(config['buyer_password'])
    login_page.click_login()

    login_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source


def test_missing_password(driver, config):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)

    login_page.enter_phone_number(config['buyer_phone_number'])
    login_page.enter_password("")
    login_page.click_login()

    login_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source


def test_wrong_password(driver, config):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)

    login_page.enter_phone_number(config['buyer_phone_number'])
    login_page.enter_password("KimOanh2003@")
    login_page.click_login()

    login_page.wait_for_text("Mật khẩu không đúng. Vui lòng kiểm tra lại")

    assert "Mật khẩu không đúng. Vui lòng kiểm tra lại" in driver.page_source


def test_phone_number_not_registered(driver, config):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)
    phone_number = "0905656187"

    login_page.enter_phone_number(phone_number)
    login_page.enter_password("Kimoanh2003@")
    login_page.click_login()

    user = login_page.get_user_by_phone_number_from_db(phone_number)
    assert user is None, f"User with phone number {phone_number} is already registered"


def test_successful_login(driver, config):
    driver.get(config["base_url"])
    driver.maximize_window()

    home_page = HomePage(driver, config)
    home_page.click_login_btn()

    login_page = LoginPage(driver, config)

    login_page.enter_phone_number(config['buyer_phone_number'])
    login_page.enter_password(config['buyer_password'])
    login_page.click_login()
