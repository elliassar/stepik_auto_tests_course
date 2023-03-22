# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     result = str(math.ceil(math.pow(math.pi, math.e) * 10000))
#
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     link = browser.find_element(By.LINK_TEXT, result)
#     link.click()
#
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла


########


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла


########


# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#
#     button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# #не забываем оставить пустую строку в конце файла


########

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(5)
browser.quit()