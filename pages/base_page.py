import time
from configparser import SectionProxy

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from sqlalchemy.orm import Session


class BasePage:
    def __init__(self, driver: WebDriver, config: SectionProxy, db: Session | None = None, timeout: int = 10):
        self.driver = driver
        self.db = db
        self.config = config
        self.timeout = timeout

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.find_element(locator).click()
        time.sleep(3)

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

    def set_session_id(self):
        self.driver.get(self.config['base_url'])
        self.driver.add_cookie(cookie_dict={
            'name': 'sessionid',
            'value': self.config['sessionid'],
        })
