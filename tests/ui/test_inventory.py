import pytest
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage

pytestmark = pytest.mark.ui


def test_inventory_has_exactly_6_items(driver, wait, config):
    login = LoginPage(driver, wait, config["sauce_url"]).open()
    login.login_as(config["sauce_username"], config["sauce_password"])

    inventory = InventoryPage(driver, wait).wait_until_loaded()
    items = inventory.get_items()
    assert len(items) == 6, f"Expected 6 items, got {len(items)}"


def test_add_first_item_shows_badge_one(driver, wait, config):
    login = LoginPage(driver, wait, config["sauce_url"]).open()
    login.login_as(config["sauce_username"], config["sauce_password"])

    inventory = InventoryPage(driver, wait).wait_until_loaded()
    inventory.add_first_item_to_cart()
    assert inventory.get_cart_badge_text() == "1"
