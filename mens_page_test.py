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


def test_nike_men(page, nike_url):
    page.goto(nike_url)
    expect(page).to_have_url(nike_url)

    mens_link = page.get_by_role("link", name="Men", exact=True)
    mens_link.click()

    expect(page).to_have_url("https://www.nike.com/il/men")
    time.sleep(5)
