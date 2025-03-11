from playwright.sync_api import Page, expect, Route
import re
import json


def test_change_request(page: Page):
    new_product_name = "яблокофон 16 про"

    def change_req(route: Route):
        response = route.fetch()
        response_data = response.json()
        items = response_data["body"]["digitalMat"]
        for item in items:
            if item["productName"] == "iPhone 16 Pro":
                for family_type in item["familyTypes"]:
                    if family_type["productName"] == "iPhone 16 Pro":
                        family_type["productName"] = new_product_name
        body = json.dumps(response_data)
        route.fulfill(response=response, body=body)

    page.route(re.compile("/digital-mat"), change_req)
    page.goto("https://www.apple.com/shop/buy-iphone")
    page.locator("h3", has_text="iPhone 16 Pro Max").click()
    header = page.locator("[data-autom='DigitalMat-overlay-header-0-0']")
    expect(header).to_have_text(new_product_name)
