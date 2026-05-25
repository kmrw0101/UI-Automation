# 📘 Playwright Test Suite Overview

This project demonstrates three core types of automated tests commonly used in modern QA engineering: **UI Navigation**, **Form Interaction**, and **API + UI Integration**. Together, these represent a balanced, real‑world automation strategy used across SaaS, fintech, healthcare, e‑commerce, and enterprise applications.

---

# ▶️ How to Run the Playwright Tests

1. Activate your virtual environment:  
`.\.venv\Scripts\Activate.ps1`

2. Move into the Playwright project folder:  
`cd playwright`

------------------------------------------------------------
**Standard Test Run (Headless)**  
Runs fast with no visible browser. Ideal for CI pipelines and quick checks.  
`pytest -s`

------------------------------------------------------------
**Headed Mode (Watch the Browser Work)**  
Opens a real browser window so you can visually watch the automation click,  
type, navigate, and interact with the UI. Great for debugging.  
`pytest -s --headed`

------------------------------------------------------------
**Run With Tracing Enabled**  
Records a full trace of each test: DOM snapshots, network calls, console logs,  
and a step-by-step replay you can open later. Perfect for debugging failures.  
`pytest -s --headed --tracing=on`

------------------------------------------------------------
**Opening Trace Files**  
After running with tracing enabled, Playwright stores traces in:  
`playwright/test-results/<test-folder>/trace.zip`  
Each test gets its own folder, which prevents overwriting.

Use these commands to open the actual trace files:

`python -m playwright show-trace "test-results/tests-test-basic-navigation-py-test-homepage-title-chromium/trace.zip"`  
`python -m playwright show-trace "test-results/tests-test-form-interaction-py-test-search-box-chromium/trace.zip"`  
`python -m playwright show-trace "test-results/tests-test-api-and-ui-py-test-api-drives-ui-chromium/trace.zip"`

------------------------------------------------------------
**What These Outputs Do**

**Headless Mode:**  
  - Fastest execution  
  - No visible browser  
  - Best for pipelines and automation  

**Headed Mode:**  
  - Opens a real browser window  
  - Lets you watch the automation run in real time  
  - Useful for debugging and demos  

**Trace Files:**  
  - Saved as `trace.zip` inside each test-results folder  
  - Opened with `playwright show-trace`  
  - Provides a full replay of the test:  
      • DOM snapshots  
      • Network requests  
      • Console logs  
      • Timeline of actions  
  - Essential for diagnosing failures or understanding test behavior  

---

## 🧭 1. UI Navigation Tests

**Purpose:**  
Validate that key pages load correctly and the application is reachable.

**What these tests do:**  
- Navigate to a page  
- Confirm the page loads  
- Validate the title or a key element  

**Why they matter:**  
- Fast, reliable smoke tests  
- Catch broken deployments immediately  
- Ensure the application is “alive” before deeper tests run  

**When to use:**  
- CI/CD smoke checks  
- Basic uptime validation  
- Early detection of routing or deployment issues  

**Example behaviors:**  
- Opening the homepage  
- Verifying the title  
- Ensuring no critical errors appear  

---

## 📝 2. Form Interaction Tests

**Purpose:**  
Validate that users can interact with UI elements and complete workflows.

**What these tests do:**  
- Fill input fields  
- Click buttons  
- Submit forms  
- Validate navigation or results  

**Why they matter:**  
- Represent real user behavior  
- Catch UI regressions early  
- Validate selectors, inputs, and workflows  

**When to use:**  
- Login flows  
- Search flows  
- Checkout or multi‑step forms  
- Any user‑driven interaction  

**Example behaviors:**  
- Typing into a search box  
- Pressing Enter  
- Confirming the resulting page is correct  

---

## 🔗 3. API + UI Integration Tests

**Purpose:**  
Validate that backend data and frontend UI stay in sync — a critical part of real‑world QA.

**What these tests do:**  
- Call a backend API  
- Extract data from the response  
- Navigate the UI  
- Confirm the UI displays the same data  

**Why they matter:**  
- Catch mismatches between backend and frontend  
- Validate business logic end‑to‑end  
- Ensure data integrity  
- Provide extremely high value in enterprise QA  

**When to use:**  
- Dashboards  
- Search results  
- Data‑driven pages  
- Any feature where backend → frontend consistency matters  

**Example behaviors:**  
- Fetching a post title from an API  
- Navigating to the UI page that displays posts  
- Verifying the UI shows the same title  

---

## 🧩 Why All Three Test Types Matter

A healthy automation suite includes **all three**, because each covers a different layer of risk:

| Test Type | What It Protects | Speed | Value |
|----------|-------------------|-------|--------|
| **UI Navigation** | Basic availability | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **Form Interaction** | User workflows | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **API + UI Integration** | Data correctness + business logic | ⭐⭐ | ⭐⭐⭐⭐⭐ |

Using all three gives you:

- Fast feedback  
- Realistic user coverage  
- Backend + frontend validation  
- High confidence in releases
