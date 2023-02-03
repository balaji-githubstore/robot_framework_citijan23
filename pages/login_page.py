from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class LoginPage(WebDriverKeywords):
    __driver = None

    __username_locator = (By.ID, "authUser")
    __password_locator = (By.CSS_SELECTOR, "#clearPass")
    __login_locator = (By.CSS_SELECTOR, "#login-button")
    __error_locator = (By.XPATH, "//*[contains(text(),'Invalid')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver

    def enter_username(self, username):
        # self.__driver.find_element(By.ID, "authUser").send_keys(username)
        super().send_keys_element(self.__username_locator, username)

    def enter_password(self, password):
        # self.__driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)
        super().send_keys_element(self.__password_locator, password)

    def click_login(self):
        # self.__driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        super().click_element(self.__login_locator)

    def get_error_message(self):
        # return self.__driver.find_element(By.XPATH, "//*[contains(text(),'Invalid')]").text
        super().get_text_element(self.__error_locator)

    def get_username_placeholder(self):
        # return self.__driver.find_element(By.ID, "authUser").get_attribute("placeholder")
        return super().get_attribute_element(self.__username_locator, "placeholder")

    def get_password_placeholder(self):
        # return self.__driver.find_element(By.ID, "clearPass").get_attribute("placeholder")
        return super().get_attribute_element(self.__password_locator, "placeholder")
