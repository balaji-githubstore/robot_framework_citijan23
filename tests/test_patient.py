import time
from selenium import webdriver

from selenium.webdriver.common.by import By

from base.webdriver_listner import WebDriverWrapper


class TestPatient(WebDriverWrapper):
    def test_add_patient(self):
        self.driver.find_element(By.ID, "authUser").send_keys("admin")
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys("pass")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        # use below code to handle menu on this page
        self.driver.find_element(By.XPATH, "//div[text()='Patient']").click()
        self.driver.find_element(By.XPATH, "//div[text()='New/Search']").click()

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

        # check and add wait condition before handling alert
        actual_alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()

        #click on close happy birthday

        #assert the patient name added

        time.sleep(2)
