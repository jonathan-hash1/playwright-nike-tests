import time

import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def nike_url():
    return "https://www.nike.com/il/"

def test_searchbar(page):
    page.goto("https://www.nike.com/il/")

    search = page.get_by_role("searchbox")
    search.fill("shirt")
    search.press("Enter")

    first_product = page.locator("[data-testid='product-card']").first
    expect(first_product).to_be_visible()
    first_product.click()
