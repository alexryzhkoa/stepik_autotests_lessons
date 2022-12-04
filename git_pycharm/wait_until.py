from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, "10").until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.CSS_SELECTOR, "button#book").click()
    browser.execute_script("window.scrollBy(0, 200);")
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    print(x)
    def calc(x):
        return math.log(abs(12 * math.sin(int(x))))
    enter_value = calc(x)
    print(enter_value)
    input_field = browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(enter_value)
    submit = browser.find_element(By.CSS_SELECTOR, "#solve").click()
    alert_text = browser.switch_to.alert.text
    print(alert_text.split(": ")[-1])
    browser.switch_to.alert.accept()
finally:
    time.sleep(3)
