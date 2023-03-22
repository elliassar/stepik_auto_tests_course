from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    num1 = browser.find_element(By.ID, "input_value")
    num1_value = num1.text
    result = calc(num1_value)
    print(num1_value, result)

    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(result)

    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()