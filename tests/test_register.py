from pages.register_page import RegisterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_phone_number_no_special_chars(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("07842534@6")
    register_page.enter_password("Oanh2003@")
    register_page.enter_confirm_password("Oanh2003@")
    register_page.click_register()

    register_page.wait_for_text("Số điện thoại này không hợp lệ.")

    assert "Số điện thoại này không hợp lệ." in driver.page_source


def test_phone_number_no_whitespace(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0784 356 345")
    register_page.enter_password("Kimoanh2003@")
    register_page.enter_confirm_password("Kimoanh2003@")
    register_page.click_register()

    register_page.wait_for_text("Số điện thoại này không hợp lệ.")

    assert "Số điện thoại này không hợp lệ." in driver.page_source


def test_phone_number_invalid_length(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("07842534611")
    register_page.enter_password("Kimoanh2003@")
    register_page.enter_confirm_password("Kimoanh2003@")
    register_page.click_register()

    register_page.wait_for_text("Số điện thoại này không hợp lệ.")

    assert "Số điện thoại này không hợp lệ." in driver.page_source


def test_phone_repeated_digits(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    register_url = base_url + "auth/register"
    driver.get(register_url)

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0000000000")
    register_page.enter_password("Kimoanh2003@")
    register_page.enter_confirm_password("Kimoanh2003@")
    register_page.click_register()

    register_page.wait_for_text("")

    assert "" in driver.page_source


def test_phone_invalid_format(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("123456789")
    register_page.enter_password("Kimoanh2003@")
    register_page.enter_confirm_password("Kimoanh2003@")
    register_page.click_register()

    register_page.wait_for_text("Số điện thoại này không hợp lệ.")

    assert "Số điện thoại này không hợp lệ." in driver.page_source


def test_phone_already_registered(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0784253460")
    register_page.enter_password("Kimoanh2003@")
    register_page.enter_confirm_password("Kimoanh2003@")
    register_page.click_register()

    register_page.wait_for_text("Số điện thoại này đã tồn tại.")

    assert "Số điện thoại này đã tồn tại." in driver.page_source


def test_password_digit_only(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0785654459")
    register_page.enter_password("12345678")
    register_page.enter_confirm_password("12345678")
    register_page.click_register()

    register_page.wait_for_text("Mật khẩu này quá phổ biến.")
    register_page.wait_for_text("Mật khẩu này hoàn toàn là số.")
    register_page.wait_for_text("Mật khẩu chứa ít nhất một chữ in hoa.")

    assert "Mật khẩu này quá phổ biến." in driver.page_source
    assert "Mật khẩu này hoàn toàn là số." in driver.page_source
    assert "Mật khẩu chứa ít nhất một chữ in hoa." in driver.page_source


def test_password_lowercase_only(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0905655345")
    register_page.enter_password("ababababbaba")
    register_page.enter_confirm_password("ababababbaba")
    register_page.click_register()

    register_page.wait_for_text("Mật khẩu chứa ít nhất một chữ in hoa.")

    assert "Mật khẩu chứa ít nhất một chữ in hoa." in driver.page_source


def test_password_uppercase_only(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0987665465")
    register_page.enter_password("ABABABABABAA")
    register_page.enter_confirm_password("ABABABABABAA")
    register_page.click_register()

    register_page.wait_for_text("Mật khẩu chứa ít nhất một in thường.")

    assert "Mật khẩu chứa ít nhất một in thường." in driver.page_source


def test_password_special_chars_only(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0905655345")
    register_page.enter_password("@#$%^&*!")
    register_page.enter_confirm_password("@#$%^&*!")
    register_page.click_register()

    register_page.wait_for_text("Mật khẩu chứa ít nhất một chữ in hoa.")

    assert "Mật khẩu chứa ít nhất một chữ in hoa." in driver.page_source


def test_password_no_lowercase_and_special_chars(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0905655345")
    register_page.enter_password("ABCD1234")
    register_page.enter_confirm_password("ABCD1234")
    register_page.click_register()

    register_page.wait_for_text("Mật khẩu này quá phổ biến.")
    register_page.wait_for_text("Mật khẩu chứa ít nhất một in thường.")

    assert "Mật khẩu này quá phổ biến." in driver.page_source
    assert "Mật khẩu chứa ít nhất một in thường." in driver.page_source


def test_password_no_letters(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0905655345")
    register_page.enter_password("1234@#$%")
    register_page.enter_confirm_password("1234@#$%")
    register_page.click_register()

    register_page.wait_for_text("Mật khẩu chứa ít nhất một chữ in hoa.")

    assert "Mật khẩu chứa ít nhất một chữ in hoa." in driver.page_source


def test_password_no_uppercase_and_digits(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0905655345")
    register_page.enter_password("abcd@#$%")
    register_page.enter_confirm_password("abcd@#$%")
    register_page.click_register()

    register_page.wait_for_text("Mật khẩu chứa ít nhất một chữ in hoa.")

    assert "Mật khẩu chứa ít nhất một chữ in hoa." in driver.page_source


def test_password_no_digits_no_special(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0905655345")
    register_page.enter_password("abcdABCD")
    register_page.enter_confirm_password("abcdABCD")
    register_page.click_register()

    register_page.wait_for_text("Mật khẩu chứa ít nhất một số.")

    assert "Mật khẩu chứa ít nhất một số." in driver.page_source


def test_password_no_digits_no_lowercase(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0905655345")
    register_page.enter_password("ABCD@#$%")
    register_page.enter_confirm_password("ABCD@#$%")
    register_page.click_register()

    register_page.wait_for_text("Mật khẩu chứa ít nhất một in thường.")

    assert "Mật khẩu chứa ít nhất một in thường." in driver.page_source


def test_password_with_not_space(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0905655345")
    register_page.enter_password("P@ss w0rd1")
    register_page.enter_confirm_password("P@ss w0rd1")
    register_page.click_register()

    register_page.wait_for_text("Mật khẩu không được chứa khoảng cách .")

    assert "Mật khẩu không được chứa khoảng cách ." in driver.page_source


def test_missing_confirm_password(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0905655345")
    register_page.enter_password("P@ssw0rd1")
    register_page.enter_confirm_password("")
    register_page.click_register()

    register_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source


def test_password_mismatch_with_confirm(driver, config):
    base_url = config.get("base_url", "http://localhost:8000/")
    driver.get(base_url + "auth/register")

    register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))

    register_page.enter_phone_number("0905655345")
    register_page.enter_password("P@ssw0rd1")
    register_page.enter_confirm_password("L@ssw0rd1")
    register_page.click_register()

    register_page.wait_for_text("Mật khẩu nhập lại không giống với mật khẩu trước")

    assert "Mật khẩu nhập lại không giống với mật khẩu trước" in driver.page_source

# def test_success_register(driver, config):
#     base_url = config.get("base_url", "http://localhost:8000/")
#     register_url = base_url + "auth/register"
#     driver.get(register_url)
#
#     register_page = RegisterPage(driver, timeout=int(config.get("timeout", 5)))
#
#     register_page.enter_phone_number("0905655345")
#     register_page.enter_password("P@ssw0rd1")
#     register_page.enter_confirm_password("P@ssw0rd1")
#     register_page.click_register()
#
#     WebDriverWait(driver, 3).until(EC.url_contains(base_url))
#
#     assert register_url != driver.current_url, "Đăng nhập thất bại"
