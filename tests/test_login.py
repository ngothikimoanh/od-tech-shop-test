from pages.login_page import LoginPage


def test_valid_login(driver, config):
    base_url = config.get("base_url", "https://example.com")
    driver.get(base_url)

    login_page = LoginPage(driver, timeout=int(config.get("timeout", 10)))

    login_page.enter_username("testuser")
    login_page.enter_password("password123")
    login_page.click_login()

    # Thêm assert để kiểm tra kết quả đăng nhập
    # Ví dụ: Kiểm tra URL hoặc element đặc trưng xuất hiện sau đăng nhập thành công
    assert "dashboard" in driver.current_url, "Đăng nhập không thành công, không tìm thấy 'dashboard' trong URL"
