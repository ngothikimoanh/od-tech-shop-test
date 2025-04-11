from pages.profile_page import ProfilePage
from tests.conftest import database


def test_update_profile_with_invalid_email(driver, config):
    profile_page = ProfilePage(driver, config)

    profile_page.enter_email("email_sai")
    profile_page.click_update()

    profile_page.wait_for_text("Nhập địa chỉ email.")

    assert "Nhập địa chỉ email." in driver.page_source


def test_update_profile_with_invalid_phone(driver, config):
    profile_page = ProfilePage(driver, config)

    profile_page.enter_phone_number("07856453333")

    profile_page.click_update()

    profile_page.wait_for_text("Số điện thoại này không hợp lệ.")

    assert "Số điện thoại này không hợp lệ." in driver.page_source


def test_update_profile_with_empty_phone(driver, config):
    profile_page = ProfilePage(driver, config)

    profile_page.enter_phone_number("")

    profile_page.click_update()

    profile_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source


def test_points(driver, config, database):
    profile_page = ProfilePage(driver, config, db=database)
    assert profile_page.get_points() == profile_page.get_points_from_db()


def test_update_valid_profile(driver, config):
    profile_page = ProfilePage(driver, config)

    profile_page.enter_phone_number("0914406376")
    profile_page.enter_last_name("Oanh")
    profile_page.enter_first_name("Kim")
    profile_page.enter_email("user@example.com")
    profile_page.click_update()

    profile_page.wait_for_text("Cập nhật thông tin thành công.")

    assert "Cập nhật thông tin thành công." in driver.page_source
