import time

import pytest
from playwright.sync_api import sync_playwright, expect, Locator


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
