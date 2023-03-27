import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_the_button(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')