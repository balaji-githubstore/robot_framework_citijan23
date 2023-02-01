import pytest
from selenium import webdriver


class WebDriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # will run before each test method
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://demo.openemr.io/b/openemr")
        yield
        # will run after each test method always
        self.driver.quit()

