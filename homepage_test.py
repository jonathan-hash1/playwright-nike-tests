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


def test_nike_homepage(page, nike_url):
    page.goto(nike_url)

    expect(page).to_have_url(nike_url)

    expect(page).to_have_url('https://www.nike.com/il/')
