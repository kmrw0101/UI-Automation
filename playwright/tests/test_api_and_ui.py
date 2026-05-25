"""
App: API + UI Integration Test (Playwright)

This test demonstrates a real-world workflow where API data is used
to drive UI validation. It fetches a post from a public API and then
verifies that the same content appears in the UI. This pattern is
common in modern automation frameworks where backend and frontend
validation work together.

This script handles:
- Calling a REST API using Playwright's page.request API client
- Parsing JSON response data
- Navigating the UI
- Validating that API-driven content appears in the UI

Sections:
- Imports
- Test: API Drives UI
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from playwright.sync_api import Page, expect


# ---------------------------------------------------------------------------
# Test: API Drives UI
# ---------------------------------------------------------------------------
# This test:
# - Calls a public API using page.request
# - Extracts the title from the JSON response
# - Navigates the UI to the posts page
# - Validates that the post title appears in the UI
# ---------------------------------------------------------------------------
def test_api_drives_ui(page: Page):
    response = page.request.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    data = response.json()

    page.goto("https://jsonplaceholder.typicode.com/")

    # More specific locator: click the /posts link
    page.get_by_role("link", name="/posts").first.click()

    expect(page.get_by_text(data["title"])).to_be_visible()
