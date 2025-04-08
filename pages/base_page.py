from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)
