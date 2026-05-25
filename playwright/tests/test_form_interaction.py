"""
App: Form Interaction Test (Playwright)

This test demonstrates interacting with UI elements such as input
fields and validating navigation behavior. It uses Wikipedia's
search box to show how Playwright handles typing, key presses, and
URL assertions.

This script handles:
- Navigating to Wikipedia
- Locating the search field using a stable CSS selector (input#searchInput)
- Filling a search field
- Submitting the form via keyboard interaction
- Validating the resulting URL

Sections:
- Imports
- Test: Search Box Interaction
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
# Provides the Page object and expect assertions for UI validation.
# ---------------------------------------------------------------------------
import re
from playwright.sync_api import Page, expect


# ---------------------------------------------------------------------------
# Test: Search Box Interaction
# ---------------------------------------------------------------------------
# This test:
# - Navigates to Wikipedia
# - Locates the search box using a stable CSS selector
# - Types a query and presses Enter
# - Validates that the resulting URL contains the search term
# ---------------------------------------------------------------------------
def test_search_box(page: Page):
    page.goto("https://www.wikipedia.org/")
    search = page.locator("input#searchInput")
    search.fill("Playwright")
    search.press("Enter")

    expect(page).to_have_url(re.compile("Playwright"))
