import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.online.citibank.co.in/")

driver.find_element(By.XPATH,"//a[@title='Close']").click()
driver.find_element(By.XPATH,"//span[text()='Login']").click()

print(driver.window_handles)
# print(driver.window_handles[0])
# print(driver.window_handles[1])

#switch to 2nd tab
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH,"//div[contains(text(),'Forgot User')]").click()

# 5.	Choose Credit Card
# 6.	Enter credit card number as 4545 5656 8887 9998
# 7.	Enter cvv number
# 8.	Enter date as “14/04/2022”
driver.execute_script("document.querySelector('#bill-date-long').value='14/04/2000'")
# 9.	Click on Proceed
# 10.	 Get the text and print it “Please accept Terms and Conditions”


time.sleep(3)
driver.quit()
