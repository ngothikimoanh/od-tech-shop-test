from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_missing_phone_number(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/login")

    login_page = LoginPage(driver, timeout=int(config.get("timeout", 10)))

    login_page.enter_phone_number("")
    login_page.enter_password("Kimoanh2003@")
    login_page.click_login()

    assert "Số điện thọai không được bỏ trống" in driver.page_source, "Đăng nhập thất bại"


def test_missing_pasword(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/login")

    login_page = LoginPage(driver, timeout=int(config.get("timeout", 10)))

    login_page.enter_phone_number("0784253460")
    login_page.enter_password("")
    login_page.click_login()

    assert "Mật khẩu không được bỏ trống" in driver.page_source, "Đăng nhập thất bại"


def test_phone_number_is_not_registered(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/login")

    login_page = LoginPage(driver, timeout=int(config.get("timeout", 10)))

    login_page.enter_phone_number("0784255344")
    login_page.enter_password("Oanh123@")
    login_page.click_login()
    error_message = login_page.get_error_message()

    WebDriverWait(driver, 3).until(EC.url_contains("http://localhost:8000/auth/login"))
    assert error_message == "Số điện thoại này chưa được đăng ký.", "Đăng nhập thất bại"


def test_success_login(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    login_url = base_url + "auth/login"
    driver.get(login_url)

    login_page = LoginPage(driver, timeout=int(config.get("timeout", 10)))

    login_page.enter_phone_number("0784253460")
    login_page.enter_password("Kimoanh2003@")
    login_page.click_login()

    WebDriverWait(driver, 3).until(EC.url_contains("http://localhost:8000/"))
    assert login_url != driver.current_url, "Đăng nhập thất bại"