import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.base_page import BasePage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(100)
    driver.get(BasePage.url)
    yield driver
    driver.quit()

