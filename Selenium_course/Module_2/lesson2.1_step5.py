from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.XPATH, '// *[ @ id = "treasure"]')
    treasure_value = treasure.get_attribute("valuex")

    input = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input.send_keys(calc(treasure_value))

    option1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    option1.click()

    option2 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    option2.click()

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

