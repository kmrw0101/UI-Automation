"""
App: Basic Navigation Test (Playwright)

This test demonstrates the simplest form of UI automation:
navigating to a webpage and validating the page title. It serves
as a foundational example for understanding Playwright's sync API
and assertion model.

This script handles:
- Opening a webpage
- Waiting for the page to load
- Validating the page title using Playwright's expect API

Sections:
- Imports
- Test: Homepage Title
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
# Playwright's sync API provides the Page object and expect assertions.
# ---------------------------------------------------------------------------
from playwright.sync_api import Page, expect


# ---------------------------------------------------------------------------
# Test: Homepage Title
# ---------------------------------------------------------------------------
# This test navigates to example.com and verifies the page title.
# It demonstrates:
# - Basic navigation
# - Auto-waiting behavior
# - Simple assertions
# ---------------------------------------------------------------------------
def test_homepage_title(page: Page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")
