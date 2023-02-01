import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")

driver.find_element(By.NAME,"UserFirstName").send_keys("john")
driver.find_element(By.NAME,"UserLastName").send_keys("ken")

select_job=Select(driver.find_element(By.NAME,"UserTitle"))
select_job.select_by_visible_text("IT Manager")

select_employees=Select(driver.find_element(By.XPATH,"//select[contains(@id,'CompanyEmployees')]"))
select_employees.select_by_value("250")

#click on submit
driver.find_element(By.NAME,"start my free trial").click()
time.sleep(3)



