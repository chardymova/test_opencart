import pytest
import logging
from datetime import datetime
from selenium import webdriver
from variables import url
from selenium.webdriver.support.events import (AbstractEventListener,
                                               EventFiringWebDriver)


class CustomEventListener(AbstractEventListener):
    def __init__(self, request=None):
        self.request = request

    def before_find(self, by, value, driver):
        logging.info(f"Search element with '{by}={value}' on {driver.current_url}\n")

    def on_exception(self, exception, driver):
        current_time = datetime.now().strftime("%d_%B_%Y_%I_%M_%S")

        driver.get_screenshot_as_file(
            'screenshots/' + self.request.module.__name__ + '-' +
            self.request.function.__name__ + '_' + current_time + '.png')
        logging.critical(
            f"Exception '{exception}' on {driver.current_url} "
            f"in {self.request.module.__name__} {self.request.function.__name__}")


def pytest_configure(config):
    if not config.option.log_file:
        current_time = datetime.now().strftime("%d_%B_%Y_%I_%M_%S")
        config.option.log_file = 'logs/log.' + current_time


def pytest_addoption(parser):
    parser.addoption('--address', action='store', default=url)
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture
def address_param(request):
    return request.config.getoption('--address')


@pytest.fixture
def browser_param(request):
    return request.config.getoption('--browser')


@pytest.fixture
def driver(request, browser_param):
    if browser_param.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser_param.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser_param.lower() == 'edje':
        driver = webdriver.Edge()
    event_listener = CustomEventListener(request=request)
    driver = EventFiringWebDriver(driver, event_listener)

    def fin():
        log = driver.get_log('browser')
        for i in log:
            try:
                message_er = i['message']
                type_er = i['level']
                logging.warning(f"Message '{message_er}' - Type {type_er} ")
            except:
                continue
        driver.quit()

    request.addfinalizer(fin)
    return driver
