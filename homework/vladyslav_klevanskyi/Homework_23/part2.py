from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

# Data
first_name = "Arni"
last_name = "Max"
email = "arni.max@example.com"
gender = "Male"
phone = "1234567890"
date = "24 Feb 2022"
subjects = ["Maths", "English"]
address = "123 Main St, City, Country"
state = "NCR"
city = "Delhi"

# Get page
driver.get("https://demoqa.com/automation-practice-form")

# Finding elements
first_name_field = driver.find_element(By.ID, "firstName")
last_name_field = driver.find_element(By.ID, "lastName")
email_field = driver.find_element(By.ID, "userEmail")
male_radio = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
phone_field = driver.find_element(By.ID, "userNumber")
date_field = driver.find_element(By.ID, "dateOfBirthInput")
subjects_field = driver.find_element(By.ID, "subjectsInput")
sport_checkbox = driver.find_element(
    By.XPATH,
    "//label[@for='hobbies-checkbox-1']"
)
music_checkbox = driver.find_element(
    By.XPATH,
    "//label[@for='hobbies-checkbox-3']"
)
address_field = driver.find_element(
    By.XPATH,
    "//textarea[@placeholder='Current Address']"
)
select_state = driver.find_element(By.ID, "react-select-3-input")
select_city = driver.find_element(By.ID, "react-select-4-input")
submit_button = driver.find_element(By.ID, "submit")

# Fill out the form
first_name_field.send_keys(first_name)
last_name_field.send_keys(last_name)
email_field.send_keys(email)
male_radio.click()
phone_field.send_keys(phone)

date_field.click()
select_year = driver.find_element(
    By.CLASS_NAME,
    "react-datepicker__year-select"
)
select_year.send_keys("2022")
select_month = driver.find_element(
    By.CLASS_NAME,
    "react-datepicker__month-select"
)
select_month.send_keys("February")
select_day = driver.find_element(By.CLASS_NAME, "react-datepicker__day--024")
select_day.click()

subjects_field.click()
for subject in subjects:
    subjects_field.send_keys(subject)
    subjects_field.send_keys(Keys.ENTER)

sport_checkbox.click()
music_checkbox.click()

address_field.send_keys(address)

select_state.send_keys(state)
select_state.send_keys(Keys.ENTER)
select_city.send_keys(city)
select_city.send_keys(Keys.ENTER)

submit_button.click()

table_body = driver.find_element(By.TAG_NAME, "tbody")
table_rows = table_body.find_elements(By.TAG_NAME, "tr")
for row in table_rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    print(columns[0].text + ": " + columns[1].text)
