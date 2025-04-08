import configparser
import os
import sys

import pytest
from selenium import webdriver

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


@pytest.fixture(scope="session")
def config():
    config = configparser.ConfigParser()
    config_file_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.ini")
    config.read(config_file_path)
    return config["DEFAULT"]


@pytest.fixture(scope="function")
def driver(config):
    driver = webdriver.Chrome()
    driver.implicitly_wait(int(config.get("timeout", 10)))
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call and request.node.rep_call.failed:
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        screenshot_file = os.path.join(screenshots_dir, f"{request.node.name}.png")
        driver.save_screenshot(screenshot_file)
        print(f"\nScreenshot saved at: {screenshot_file}")
