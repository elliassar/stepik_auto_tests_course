from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()



    num1 = browser.find_element(By.ID, "input_value")
    num1_value = num1.text
    result = calc(num1_value)
    print(num1_value, result)


    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(result)


    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button.click()


finally:
    time.sleep(8)
    browser.quit()