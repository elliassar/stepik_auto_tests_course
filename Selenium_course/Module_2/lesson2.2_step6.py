from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "input_value")
    num1_value = num1.text
    print(num1_value)

    result = calc(num1_value)
    print(result)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 150);")


    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(result)


    option1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    option1.click()


    option2 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    option2.click()


    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()