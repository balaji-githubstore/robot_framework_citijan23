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
driver.find_element(By.LINK_TEXT,"APPLY FOR CREDIT CARDS").click()


print(driver.window_handles)

for win in driver.window_handles:
    driver.switch_to.window(win)
    if driver.title=="Citibank India":
        break

print("---------")
driver.close()


time.sleep(3)
driver.quit()
