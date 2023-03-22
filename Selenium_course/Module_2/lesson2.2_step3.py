from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num1_value = num1.text
    print(num1_value)

    num2 = browser.find_element(By.ID, "num2")
    num2_value = num2.text
    print(num2_value)

    result = str(int(num1_value) + int(num2_value))
    print(result)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)

    button = browser.find_element(By.XPATH, "/html/body/div/form/button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()