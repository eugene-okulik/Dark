from playwright.sync_api import Page, expect


def test_get_by_role(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    page.get_by_role("textbox", name="username").fill("tomsmith")
    page.get_by_role("textbox", name="password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="login").click()
    expect(page.get_by_role("heading", name="Secure Area.")).to_be_visible()
