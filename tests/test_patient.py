import time

import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_listner import WebDriverWrapper
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestPatient(WebDriverWrapper):
    @pytest.mark.smoke
    @pytest.mark.patient
    def test_add_patient(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("admin")
        login_page.enter_password("pass")
        login_page.click_login()

        # use below code to handle menu on this page
        main_page=MainPage(self.driver)
        main_page.click_patient()
        main_page.click_new_search()

        #SearchOrAddPatientPage
        #start

        # action=webdriver.ActionChains(self.driver)
        # action.move_to_element(self.driver.find_element(By.XPATH, "//div[text()='Patient']")).perform()

        # self.driver.find_element(By.XPATH, "//div[text()='New/Search']").click()
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@name='modalframe']"))

        self.driver.find_element(By.ID, "form_fname").send_keys("john")
        # enter lastname as wick
        # enter dob
        self.driver.find_element(By.ID, "form_DOB").send_keys("2023-02-01")
        # select gender
        # click on create new patient

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
        # clickon Confirm Create New Patient
        self.driver.switch_to.default_content()

        # explicit wait - exact condition
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.alert_is_present())

        # check and add wait condition before handling alert
        actual_alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()

        #click on close happy birthday
        # wait.until(expected_conditions.visibility_of_element_located((By.ID,"authUser"))).click()

        # end - handle under SearchOrAddPatientPage

        #PatientDashboardPage
        # get the patient name

        #below present here

        #assert the patient name added
        #assert the alert text contains Tobacco

        time.sleep(2)
