import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from utilities import data_source

from base.webdriver_listner import WebDriverWrapper


class TestLogin(WebDriverWrapper):
    @pytest.mark.parametrize(
        "username,password,expected_title",
        data_source.valid_login_data
    )
    def test_valid_login(self, username, password, expected_title):
        self.driver.find_element(By.ID, "authUser").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        assert_that(expected_title).is_equal_to(self.driver.title)

    #move the list to data_source.py module
    # @pytest.mark.parametrize("username,password,expected_error",data_source.invalid_login_data)
    @pytest.mark.parametrize("username,password,expected_error", [
        ["kim", "kim123", "Invalid username or password"],
        ["saul", "saul123", "Invalid username or password"]
    ])
    def test_invalid_login(self,username,password,expected_error):
        self.driver.find_element(By.ID, "authUser").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        actual_error = self.driver.find_element(By.XPATH, "//*[contains(text(),'Invalid')]").text
        assert_that(actual_error).contains(expected_error)


class TestLoginUI(WebDriverWrapper):
    def test_title(self):
        assert_that("OpenEMR Login").is_equal_to(self.driver.title)

    def test_application_description(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")

    def test_placeholders(self):
        actual_user_placeholder = self.driver.find_element(By.ID, "authUser").get_attribute("placeholder")
        actual_pass_placeholder = self.driver.find_element(By.ID, "clearPass").get_attribute("placeholder")
        assert_that("Username").is_equal_to(actual_user_placeholder)
        assert_that("Password").is_equal_to(actual_pass_placeholder)
