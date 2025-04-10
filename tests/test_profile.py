from selenium.webdriver.support.ui import WebDriverWait

from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC


def login_and_go_to_profile(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/login")

    login_page = LoginPage(driver, timeout=int(config.get("timeout", 10)))
    login_page.enter_phone_number("0784253460")
    login_page.enter_password("Kimoanh2003@")
    login_page.click_login()

    WebDriverWait(driver, 5).until(EC.url_contains("/"))
    driver.get(base_url + "users/profile")


def test_update_valid_profile(driver, config):
    login_and_go_to_profile(driver, config)

    profile_page = ProfilePage(driver, timeout=int(config.get("timeout", 5)))

    profile_page.enter_phone_number("0914406376")
    profile_page.enter_last_name("Oanh")
    profile_page.enter_first_name("Kim")
    profile_page.enter_email("user@example.com")
    profile_page.click_update()

    profile_page.wait_for_text("Cập nhật thông tin thành công.")

    assert "Cập nhật thông tin thành công." in driver.page_source

def test_update_profile_with_invalid_email(driver, config):
    login_and_go_to_profile(driver, config)

    profile_page = ProfilePage(driver, timeout=int(config.get("timeout", 5)))

    profile_page.enter_email("email_sai")
    profile_page.click_update()

    profile_page.wait_for_text("Nhập địa chỉ email.")

    assert "Nhập địa chỉ email." in driver.page_source

def test_update_profile_with_invalid_phone(driver, config):
    login_and_go_to_profile(driver, config)

    profile_page = ProfilePage(driver, timeout=int(config.get("timeout", 5)))

    profile_page.enter_phone_number("07856453333")

    profile_page.click_update()

    profile_page.wait_for_text("Số điện thoại này không hợp lệ.")

    assert "Số điện thoại này không hợp lệ." in driver.page_source

def test_update_profile_with_empty_phone(driver, config):
    login_and_go_to_profile(driver, config)

    profile_page = ProfilePage(driver, timeout=int(config.get("timeout", 5)))

    profile_page.enter_phone_number("")

    profile_page.click_update()

    profile_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source
# #TODO: CHECK DB
# def test_points(driver, config):
#     login_and_go_to_profile(driver, config)
#