from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture(scope="function")
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()


def test_language_select(driver):
    language = "Python"
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    button = driver.find_element(By.NAME, "submit")
    select_language = driver.find_element(By.ID, "id_choose_language")
    dropdown = Select(select_language)
    dropdown.select_by_visible_text(language)
    button.click()
    result = driver.find_element(By.ID, "result-text").text
    assert result == language


def test_start_button(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    result = driver.find_element(By.ID, "finish")
    result_text = result.find_element(By.TAG_NAME, "h4").text
    assert result_text == "Hello World!"
