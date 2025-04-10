from pages.login_page import LoginPage

def test_missing_phone_number(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/login")

    login_page = LoginPage(driver, timeout=int(config.get("timeout",5)))

    login_page.enter_phone_number("")
    login_page.enter_password("Kimoanh2003@")
    login_page.click_login()

    login_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source

def test_missing_password(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/login")

    login_page = LoginPage(driver, timeout=int(config.get("timeout",5)))

    login_page.enter_phone_number("0784253460")
    login_page.enter_password("")
    login_page.click_login()

    login_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source

def test_wrong_password(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/login")

    login_page = LoginPage(driver, timeout=int(config.get("timeout",5)))

    login_page.enter_phone_number("0784253460")
    login_page.enter_password("Oanh2003@")
    login_page.click_login()

    login_page.wait_for_text("Mật khẩu không đúng. Vui lòng kiểm tra lại")

    assert "Mật khẩu không đúng. Vui lòng kiểm tra lại" in driver.page_source

# TODO: check DB
def test_phone_number_not_registered(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/login")

    login_page = LoginPage(driver, timeout=int(config.get("timeout",5)))

    login_page.enter_phone_number("0784253461")
    login_page.enter_password("Kimoanh2003@")
    login_page.click_login()

    login_page.wait_for_text("Số điện thoại này chưa được đăng ký.")
    assert "Số điện thoại này chưa được đăng ký." in driver.page_source

# TODO: check DB
def test_successful_login(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/login")

    login_page = LoginPage(driver, timeout=int(config.get("timeout",5)))

    login_page.enter_phone_number("0784253460")
    login_page.enter_password("Kimoanh2003@")
