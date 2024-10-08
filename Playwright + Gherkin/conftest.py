# Description: This file contains the fixtures that are used in the tests.
import pytest

from playwright.sync_api import Page


@pytest.fixture()
def browser(page: Page):
    yield page
    page.close()