from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class MainPage(WebDriverKeywords):
    __driver = None

    __patient_locator=(By.XPATH, "//div[text()='Patient']")

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver

    @property
    def get_main_page_title(self):
        return self.__driver.title

    def click_patient(self):
        # self.__driver.find_element(By.XPATH, "//div[text()='Patient']").click()
        super().click_element(self.__patient_locator)

    def click_new_search(self):
        self.__driver.find_element(By.XPATH, "//div[text()='New/Search']").click()
