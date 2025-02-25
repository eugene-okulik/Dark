import pytest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.quit()


def test_first(driver):
    product_name = "Samsung galaxy s6"
    driver.get("https://www.demoblaze.com/index.html")
    # search product
    product = driver.find_element(By.XPATH, f"//a[text()='{product_name}']")
    # open product in new tab
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL)
    actions.perform()
    # go to new tab
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    # add product to cart
    driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    # close current tab and switch to main tab
    driver.close()
    driver.switch_to.window(tabs[0])
    # go to cart
    driver.find_element(By.XPATH, "//a[text()='Cart']").click()
    # check product in cart
    try:
        product_in_cart = driver.find_element(
            By.XPATH,
            f"//td[text()='{product_name}']"
        )
    except NoSuchElementException:
        product_in_cart = None
    assert product_in_cart, "Product is not in cart"


def test_second(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    # search for first product
    product = driver.find_element(By.XPATH, "//a[@class='product-item-link']")
    product_name = product.text.strip()
    # add product to compare
    actions = ActionChains(driver)
    actions.move_to_element(product).perform()
    add_to_to_compare = driver.find_element(
        By.CSS_SELECTOR,
        "a[title='Add to Compare']"
    )
    actions.click(add_to_to_compare).perform()
    # search for compare block
    compare_block = driver.find_element(
        By.XPATH,
        "//div[@class='block block-compare']"
    )
    # search for product in compare list
    try:
        product_name_in_compare = compare_block.find_element(
            By.XPATH, f"//a[text()='{product_name}']")
    except NoSuchElementException:
        product_name_in_compare = None
    assert product_name_in_compare, "Product is not in compare list"
