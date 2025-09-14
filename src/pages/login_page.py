from __future__ import annotations
from typing import TYPE_CHECKING
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

if TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver
    from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    _username = (By.ID, "user-name")
    _password = (By.ID, "password")
    _login_btn = (By.ID, "login-button")
    _error_msg = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver: 'WebDriver', wait: 'WebDriverWait', base_url: str):
        self.driver = driver
        self.wait = wait
        self.base_url = base_url.rstrip("/")

    def open(self) -> 'LoginPage':
        self.driver.get(self.base_url + "/")
        self.wait.until(EC.visibility_of_element_located(self._login_btn))
        return self

    def login_as(self, username: str, password: str):
        self.driver.find_element(*self._username).clear()
        self.driver.find_element(*self._username).send_keys(username)
        self.driver.find_element(*self._password).clear()
        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._login_btn).click()
