from pages.login_page import LoginPage
from utils.credentials import (
    VALID_USERNAME, VALID_PASSWORD,
    INVALID_USERNAME, INVALID_PASSWORD
)

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    assert "inventory" in driver.current_url


def test_login_fail_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, INVALID_PASSWORD)

    assert "Epic sadface" in login_page.get_error_message()


def test_login_fail_wrong_username(driver):
    login_page = LoginPage(driver)
    login_page.login(INVALID_USERNAME, VALID_PASSWORD)

    assert "Epic sadface" in login_page.get_error_message()


def test_login_fail_both_wrong(driver):
    login_page = LoginPage(driver)
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    assert "Epic sadface" in login_page.get_error_message()


def test_login_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.login("", "")

    assert "Epic sadface" in login_page.get_error_message()
