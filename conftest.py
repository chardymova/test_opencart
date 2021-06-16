import pytest
from selenium import webdriver
from variables import *

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
        wd=webdriver.Chrome()
    elif browser_param.lower() == 'firefox':
        wd=webdriver.Firefox()
    elif browser_param.lower() == 'edje':
        wd=webdriver.Edge()
    request.addfinalizer(wd.quit)
    return wd