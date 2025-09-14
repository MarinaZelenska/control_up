from __future__ import annotations
from typing import List, TYPE_CHECKING
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

if TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver
    from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:

    _inventory_container = (By.ID, "inventory_container")
    _inventory_items = (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    _add_to_cart_buttons = (By.CSS_SELECTOR, "button.btn_inventory")
    _cart_badge = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def wait_until_loaded(self) -> 'InventoryPage':
        self.wait.until(EC.visibility_of_element_located(self._inventory_container))
        return self

    def get_items(self) -> 'List':
        return self.driver.find_elements(*self._inventory_items)

    def add_first_item_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self._add_to_cart_buttons))
        buttons = self.driver.find_elements(*self._add_to_cart_buttons)
        assert buttons, "No Add to cart buttons found"
        buttons[0].click()

    def get_cart_badge_text(self) -> str:
        self.wait.until(EC.visibility_of_element_located(self._cart_badge))
        return self.driver.find_element(*self._cart_badge).text.strip()
