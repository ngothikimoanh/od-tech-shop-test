from pages.login_page import LoginPage


def test_missing_phone_number(driver, config):
    login_page = LoginPage(driver, config)

    login_page.enter_phone_number("")
    login_page.enter_password("Kimoanh2003@")
    login_page.click_login()

    login_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source


def test_missing_password(driver, config):
    login_page = LoginPage(driver, config)

    login_page.enter_phone_number("0784253460")
    login_page.enter_password("")
    login_page.click_login()

    login_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source


def test_wrong_password(driver, config):
    login_page = LoginPage(driver, config)

    login_page.enter_phone_number("0784253460")
    login_page.enter_password("Oanh2003@")
    login_page.click_login()

    login_page.wait_for_text("Mật khẩu không đúng. Vui lòng kiểm tra lại")

    assert "Mật khẩu không đúng. Vui lòng kiểm tra lại" in driver.page_source


def test_phone_number_not_registered(driver, config, database):
    login_page = LoginPage(driver, config, db=database)
    phone_number = "0784253461"

    user = login_page.get_user_by_phone_number_from_db(phone_number)
    assert user is None, f"User with phone number {phone_number} is already registered"

    login_page.enter_phone_number(phone_number)
    login_page.enter_password("Kimoanh2003@")
    login_page.click_login()

    login_page.wait_for_text("Số điện thoại này chưa được đăng ký.")
    assert "Số điện thoại này chưa được đăng ký." in driver.page_source


def test_successful_login(driver, config, database):
    login_page = LoginPage(driver, config, db=database)

    login_page.enter_phone_number("0914406376")
    login_page.enter_password("Kim0111@")
    login_page.click_login()

    session_id = login_page.get_session_id()
    print('\nSession ID: ', session_id)
    assert session_id is not None, "Session ID is not found"
