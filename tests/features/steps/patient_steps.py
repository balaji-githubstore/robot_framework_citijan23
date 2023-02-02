from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@when(u'I click on patient menu')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[text()='Patient']").click()


@when(u'I click on new-search menu')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[text()='New/Search']").click()


@when(u'I fill the patient detail')
def step_impl(context):

    context.driver.switch_to.frame(context.driver.find_element(By.XPATH, "//iframe[@name='pat']"))

    context.driver.find_element(By.ID, "form_fname").send_keys(context.table[0]["firstname"])
    context.driver.find_element(By.ID, "form_lname").send_keys(context.table[0]["lastname"])
    context.driver.find_element(By.ID, "form_DOB").send_keys(context.table[0]["dob"])

    select_gender = Select(context.driver.find_element(By.ID, "form_sex"))
    select_gender.select_by_visible_text(context.table[0]["gender"])


@when(u'I click on create new patient')
def step_impl(context):
    context.driver.find_element(By.ID, "create").click()
    context.driver.switch_to.default_content()


@when(u'I click on confirm create new patient')
def step_impl(context):
    print("hello")


@when(u'I store the alert text and handles it')
def step_impl(context):
    print("hello")


@when(u'I close happy birthday popup if avaiable')
def step_impl(context):
    print("hello")


@then(u'I should verify the added patient name "{expected_patient}"')
def step_impl(context, expected_patient):
    print("hello")


@then(u'I should verify the alert text contains "{text}"')
def step_impl(context, text):
    print("hello")
