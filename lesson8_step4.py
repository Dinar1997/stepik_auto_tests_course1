from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


# Открываем браузер
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

# Заполняем поля
input1 = browser.find_element(By.TAG_NAME, "button")
input1.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

x = browser.find_element(By.ID, "input_value")
x = int(x.text)
y = calc(x)

input2 = browser.find_element(By.ID, "answer")
input2.send_keys(y)

# Нажимаем кнопку
browser.find_element(By.CSS_SELECTOR, "button.btn").click()

# Закрываем браузер
time.sleep(3)
browser.quit()