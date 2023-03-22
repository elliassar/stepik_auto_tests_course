from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[1]")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[2]")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[3]")
    input3.send_keys("mail@mail.ru")

    input4 = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'info.txt')
    input4.send_keys(file_path)

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    time.sleep(8)
    browser.quit()