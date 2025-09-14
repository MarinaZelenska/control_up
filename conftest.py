import os
from typing import Dict, Any
import pytest
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from src.core_api.base_api_client import BaseApiClient

load_dotenv()


@pytest.fixture(scope="session")
def config() -> Dict[str, Any]:
    return {
        "sauce_url": os.getenv("SAUCE_URL", "https://www.saucedemo.com"),
        "sauce_username": os.getenv("SAUCE_USERNAME", "standard_user"),
        "sauce_password": os.getenv("SAUCE_PASSWORD", "secret_sauce"),
        "airport_base": os.getenv("AIRPORT_GAP_BASE", "https://airportgap.com/api"),
        "headless": os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes", "y"),
        "implicit_wait": int(os.getenv("IMPLICIT_WAIT", "0")),
        "explicit_wait": int(os.getenv("EXPLICIT_WAIT", "10")),
    }


@pytest.fixture(scope="session")
def api(config) -> BaseApiClient:
    session = requests.Session()
    client = BaseApiClient(base_url=config["airport_base"].rstrip("/"), session=session)
    yield client
    session.close()


@pytest.fixture(scope="session")
def driver(config):
    options = ChromeOptions()
    if config["headless"]:
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(options=options)

    if config["implicit_wait"]:
        drv.implicitly_wait(config["implicit_wait"])

    yield drv
    drv.quit()


@pytest.fixture
def wait(driver, config):
    from selenium.webdriver.support.ui import WebDriverWait
    return WebDriverWait(driver, config["explicit_wait"])
