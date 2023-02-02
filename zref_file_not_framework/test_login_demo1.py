# import pytest
# from selenium import webdriver
# from assertpy import assert_that
# from selenium.webdriver.common.by import By
#
# #fixture scope as class
#
# @pytest.fixture(scope="class", autouse=True)
# def setup(request):
#     # will run before each test method
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(20)
#     driver.get("https://demo.openemr.io/b/openemr")
#     request.cls.driver = driver
#     request.cls.my_name="Balaji Dinakaran"
#     yield
#     # will run after each test method always
#     driver.quit()
#
#
# class TestLoginUI:
#     def test_title(self):
#         assert_that("OpenEMR Login").is_equal_to(self.driver.title)
#
#     def test_application_description(self):
#         actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
#         assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")
#
#     def test_placeholders(self):
#         actual_user_placeholder = self.driver.find_element(By.ID, "authUser").get_attribute("placeholder")
#         actual_pass_placeholder = self.driver.find_element(By.ID, "clearPass").get_attribute("placeholder")
#         assert_that("Username").is_equal_to(actual_user_placeholder)
#         assert_that("Password").is_equal_to(actual_pass_placeholder)
