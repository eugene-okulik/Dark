from playwright.sync_api import Page, expect, BrowserContext


def test_alert(page: Page):
    page.on("dialog", lambda dialog: dialog.accept())
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.get_by_role("link", name="Click").click()
    result = page.locator("#result-text")
    expect(result).to_have_text("Ok")


def test_new_tab(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    button = page.get_by_role("link", name="Click")
    with context.expect_page() as new_tab_event:
        button.click()
    new_tab = new_tab_event.value
    text = new_tab.locator("#result-text")
    expect(text).to_have_text("I am a new page in a new tab")


def test_wait_for_color(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    button = page.get_by_role("button", name="Color Change")
    button.page.wait_for_selector(".text-danger")
    button.click()
