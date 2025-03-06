from playwright.sync_api import sync_playwright


# Data
DATA = {
    "url": "https://demoqa.com/automation-practice-form",
    "first_name": "Arni",
    "last_name": "Max",
    "email": "arni.max@example.com",
    "gender": "gender-radio-1",
    "phone": "1234567890",
    "date": ("24", "February", "2022"),
    "subjects": ["Maths", "English"],
    "address": "123 Main St, City, Country",
    "state": "NCR",
    "city": "Delhi"
}


def fill_out_the_form(
        url: str,
        first_name: str,
        last_name: str,
        email: str,
        gender: str,
        phone: str,
        date: dict,
        subjects: dict,
        address: str,
        state: str,
        city: str
):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        # Go to page
        page.goto(url)
        # Enter First Name
        page.get_by_placeholder("First Name").fill(first_name)
        # Enter Last  Name
        page.get_by_placeholder("Last Name").fill(last_name)
        # Enter Email
        page.locator("#userEmail").fill(email)
        # Choose gender
        page.locator(f"label[for='{gender}']").click()
        # Enter phone number
        page.get_by_placeholder("Mobile Number").fill(phone)
        # Select DOB
        day, month, year = date
        date_field = page.locator("#dateOfBirthInput")
        date_field.click()
        select_year = page.locator(".react-datepicker__year-select")
        select_year.click()
        select_year.select_option(year)
        select_year.click()
        select_month = page.locator(".react-datepicker__month-select")
        select_month.click()
        select_month.select_option(month)
        select_month.click()
        select_day = page.locator(".react-datepicker__day--024")
        select_day.click()
        # Select subjects
        subjects_field = page.locator("#subjectsInput")
        subjects_field.click()
        for subject in subjects:
            subjects_field.press_sequentially(subject, delay=10)
            subjects_field.press("Enter")
        # Select Hobbies
        page.locator("//label[@for='hobbies-checkbox-1']").click()
        page.locator("//label[@for='hobbies-checkbox-3']").click()
        # Enter address
        page.get_by_placeholder("Current Address").fill(address)
        # Select State and City
        select_state = page.locator("#react-select-3-input")
        select_state.press_sequentially(state)
        select_state.press("Enter")
        select_city = page.locator("#react-select-4-input")
        select_city.press_sequentially(city)
        select_city.press("Enter")
        # Sub,it the form
        page.get_by_role("button", name="Submit").click()

        # Print the table
        table_body = page.locator("tbody")
        table_rows = table_body.locator("tr")
        rows_count = table_rows.count()
        for row in range(rows_count):
            print(table_rows.nth(row).inner_text())

        browser.close()


if __name__ == "__main__":
    fill_out_the_form(**DATA)
