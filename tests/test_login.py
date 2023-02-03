import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.main_page import MainPage
from utilities import data_source
import logging

from base.webdriver_listner import WebDriverWrapper

Logger = logging.getLogger()


class TestLogin(WebDriverWrapper):
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "username,password,expected_title",
        data_source.valid_login_data
    )
    def test_valid_login(self, username, password, expected_title):
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        main_page = MainPage(self.driver)
        assert_that(expected_title).is_equal_to(main_page.get_main_page_title)

    # move the list to data_source.py module
    # @pytest.mark.parametrize("username,password,expected_error",data_source.invalid_login_data)
    @pytest.mark.parametrize("username,password,expected_error", [
        ["kim", "kim123", "Invalid username or password"],
        ["saul", "saul123", "Invalid username or password"]
    ])
    def test_invalid_login(self, username, password, expected_error):
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        actual_error = login_page.get_error_message()
        assert_that(actual_error).contains(expected_error)


class TestLoginUI(WebDriverWrapper):
    @pytest.mark.ui
    def test_title(self):
        Logger.info("Actual title " + self.driver.title)
        assert_that("OpenEMR Login").is_equal_to(self.driver.title)

    @pytest.mark.ui
    def test_application_description(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")

    @pytest.mark.ui
    def test_placeholders(self):
        login_page = LoginPage()
        actual_user_placeholder = login_page.get_username_placeholder()
        actual_pass_placeholder = login_page.get_password_placeholder()
        assert_that("Username").is_equal_to(actual_user_placeholder)
        assert_that("Password").is_equal_to(actual_pass_placeholder)
