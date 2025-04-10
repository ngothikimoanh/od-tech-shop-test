from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, config, timeout=10):
        self.driver = driver
        self.config = config
        self.timeout = timeout
        self.driver.maximize_window()
        self.base_url = config['base_url']

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)

    def wait_for_text(self, text, by=By.TAG_NAME, value="body"):
        WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element((by, value), text)
        )

    def get_text(self, locator):
        return self.driver.find_element(*locator).text
