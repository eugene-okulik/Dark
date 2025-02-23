from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

input_data = "TestText"
driver.get("https://www.qa-practice.com/elements/input/simple")
text_string = driver.find_element(By.NAME, "text_string")
text_string.send_keys(input_data)
text_string.submit()
result_text = driver.find_element(By.ID, "result-text")
print(result_text.text)
