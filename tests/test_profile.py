from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


def login_and_go_to_profile(driver, config):
    # Hàm dùng chung để đăng nhập trước khi vào trang profile
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
    profile_page = ProfilePage(driver)

    profile_page.enter_phone_number("0905123456")
    profile_page.enter_email("user@example.com")
    profile_page.enter_last_name("Nguyễn")
    profile_page.enter_first_name("Lan")
    profile_page.click_update()

    assert "Cập nhật thành công" in profile_page.get_success_message()


def test_update_profile_with_invalid_email(driver, config):
    login_and_go_to_profile(driver, config)
    profile_page = ProfilePage(driver)

    profile_page.enter_phone_number("0905123456")
    profile_page.enter_email("email_sai")
    profile_page.enter_last_name("Nguyễn")
    profile_page.enter_first_name("Lan")
    profile_page.click_update()

    assert "Email không hợp lệ" in profile_page.get_error_message()


def test_update_profile_with_invalid_phone(driver, config):
    login_and_go_to_profile(driver, config)
    profile_page = ProfilePage(driver)

    profile_page.enter_phone_number("abc123")
    profile_page.enter_email("user@example.com")
    profile_page.enter_last_name("Nguyễn")
    profile_page.enter_first_name("Lan")
    profile_page.click_update()

    assert "Số điện thoại không hợp lệ" in profile_page.get_error_message()


def test_empty_required_fields(driver, config):
    login_and_go_to_profile(driver, config)
    profile_page = ProfilePage(driver)

    profile_page.enter_phone_number("")
    profile_page.enter_email("")
    profile_page.enter_last_name("")
    profile_page.enter_first_name("")
    profile_page.click_update()

    error_msg = profile_page.get_error_message()
    assert "không được bỏ trống" in error_msg


def test_click_change_password_button(driver, config):
    login_and_go_to_profile(driver, config)
    profile_page = ProfilePage(driver)

    profile_page.click_change_password()
    WebDriverWait(driver, 3).until(EC.url_contains("/change-password"))
    assert "/change-password" in driver.current_url
