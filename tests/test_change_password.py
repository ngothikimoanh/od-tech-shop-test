from pages.change_password_page import ChangePasswordPage


def test_empty_old_password(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("")
    change_password_page.enter_new_password("Oanh2003@")
    change_password_page.enter_new_password_again("Oanh2003@")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source


def test_empty_new_password(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("")
    change_password_page.enter_new_password_again("Oanh2003@")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source


def test_empty_confirm_new_password(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("Oanh2003@")
    change_password_page.enter_new_password_again("")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Trường này là bắt buộc.")

    assert "Trường này là bắt buộc." in driver.page_source


def test_new_password_missmatch_with_confirm_new_password(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("Oanh2003@")
    change_password_page.enter_new_password_again("Kimoanh2003@")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu nhập lại không giống với mật khẩu trước")

    assert "Mật khẩu nhập lại không giống với mật khẩu trước" in driver.page_source


def test_wrong_old_password(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim2003@")
    change_password_page.enter_new_password("Oanh2003@")
    change_password_page.enter_new_password_again("Oanh2003@")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu cũ nhập không chính xác")

    assert "Mật khẩu cũ nhập không chính xác" in driver.page_source


def test_new_password_duplicates_old_password(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("Kim0111@")
    change_password_page.enter_new_password_again("Kim0111@")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu mới của bạn trùng với mật khẩu cũ")

    assert "Mật khẩu mới của bạn trùng với mật khẩu cũ" in driver.page_source


# TODO : CHANGE LANGUAGE
def test_new_password_invalid_length(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("Oanh1@")
    change_password_page.enter_new_password_again("Oanh1@")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("This password is too short. It must contain at least 8 characters.")

    assert "This password is too short. It must contain at least 8 characters." in driver.page_source


def test_new_password_digit_only(driver, config):
    change_password_page = ChangePasswordPage(driver, config)
    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("123410678")
    change_password_page.enter_new_password_again("123410678")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu này hoàn toàn là số.")
    change_password_page.wait_for_text("Mật khẩu chứa ít nhất một chữ in hoa.")

    assert "Mật khẩu này hoàn toàn là số." in driver.page_source
    assert "Mật khẩu chứa ít nhất một chữ in hoa." in driver.page_source


def test_new_password_lowercase_only(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("ababababbaba")
    change_password_page.enter_new_password_again("ababababbaba")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu chứa ít nhất một chữ in hoa.")

    assert "Mật khẩu chứa ít nhất một chữ in hoa." in driver.page_source


def test_password_uppercase_only(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("ABABABABABAA")
    change_password_page.enter_new_password_again("ABABABABABAA")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu chứa ít nhất một in thường.")

    assert "Mật khẩu chứa ít nhất một in thường." in driver.page_source


def test_password_special_chars_only(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("@#$%^&*!")
    change_password_page.enter_new_password_again("@#$%^&*!")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu chứa ít nhất một chữ in hoa.")

    assert "Mật khẩu chứa ít nhất một chữ in hoa." in driver.page_source


def test_password_no_lowercase_and_special_chars(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("ABCD1234")
    change_password_page.enter_new_password_again("ABCD1234")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu này quá phổ biến.")
    change_password_page.wait_for_text("Mật khẩu chứa ít nhất một in thường.")

    assert "Mật khẩu này quá phổ biến." in driver.page_source
    assert "Mật khẩu chứa ít nhất một in thường." in driver.page_source


def test_password_no_letters(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("1234@#$%")
    change_password_page.enter_new_password_again("1234@#$%")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu chứa ít nhất một chữ in hoa.")

    assert "Mật khẩu chứa ít nhất một chữ in hoa." in driver.page_source


def test_password_no_uppercase_and_digits(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("abcd@#$%")
    change_password_page.enter_new_password_again("abcd@#$%")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu chứa ít nhất một chữ in hoa.")

    assert "Mật khẩu chứa ít nhất một chữ in hoa." in driver.page_source


def test_password_no_digits_no_special(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("abcdABCD")
    change_password_page.enter_new_password_again("abcdABCD")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu chứa ít nhất một số.")

    assert "Mật khẩu chứa ít nhất một số." in driver.page_source


def test_password_no_digits_no_lowercase(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("ABCD@#$%")
    change_password_page.enter_new_password_again("ABCD@#$%")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu chứa ít nhất một in thường.")

    assert "Mật khẩu chứa ít nhất một in thường." in driver.page_source


def test_password_with_not_whitespace(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("P@ss w0rd1")
    change_password_page.enter_new_password_again("P@ss w0rd1")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Mật khẩu không được chứa khoảng cách.")

    assert "Mật khẩu không được chứa khoảng cách." in driver.page_source

def test_success_change_password(driver, config):
    change_password_page = ChangePasswordPage(driver, config)

    change_password_page.enter_old_password("Kim0111@")
    change_password_page.enter_new_password("Oanh2003@")
    change_password_page.enter_new_password_again("Oanh2003@")
    change_password_page.click_change_password()

    change_password_page.wait_for_text("Đổi mật khẩu thành công")

    assert "Đổi mật khẩu thành công" in driver.page_source