def get_element_text(driver, locator, timeout=10):
    """Hàm hỗ trợ lấy text của 1 element dựa trên locator."""
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    return element.text
