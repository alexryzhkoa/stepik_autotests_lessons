from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
link = "http://suninjuly.github.io/registration1.html"


def test_good_way():
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    input1.click()
    input1.send_keys("Alexey")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Ryzhko")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("ryzhkoa@mail.ru")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(3)
    browser.quit()
    if __name__ == "__main__":
        pytest.main()
