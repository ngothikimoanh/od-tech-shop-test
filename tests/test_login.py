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


# TODO: check DB
def test_phone_number_not_registered(driver, config):
    login_page = LoginPage(driver, config)

    login_page.enter_phone_number("0784253461")
    login_page.enter_password("Kimoanh2003@")
    login_page.click_login()

    login_page.wait_for_text("Số điện thoại này chưa được đăng ký.")
    assert "Số điện thoại này chưa được đăng ký." in driver.page_source


# TODO: check DB
def test_successful_login(driver, config):
    login_page = LoginPage(driver, config)

    login_page.enter_phone_number("0784253460")
    login_page.enter_password("Kimoanh2003@")
