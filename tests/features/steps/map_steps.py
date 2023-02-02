import time

from assertpy import assert_that
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I have browser with map application')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://google.com")


@when(u'I connect the cities')
def step_impl(context):
    list_of_dic = list(context.table)
    context.driver.find_element(By.NAME, "q").send_keys(len(list_of_dic))
    context.driver.find_element(By.NAME, "q").send_keys(context.table[0]["city"])
    context.driver.find_element(By.NAME, "q").send_keys(context.table[0]["statecode"])

    context.driver.find_element(By.NAME, "q").send_keys(context.table[1]["city"])
    context.driver.find_element(By.NAME, "q").send_keys(context.table[1]["statecode"])

    context.driver.find_element(By.NAME, "q").send_keys(context.table[2]["city"])
    context.driver.find_element(By.NAME, "q").send_keys(context.table[2]["statecode"])


@then(u'I should see the map with connect cities')
def step_impl(context):
    time.sleep(5)
    context.driver.quit()
