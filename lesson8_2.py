from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/selects1.html"
#http://suninjuly.github.io/selects2.html 
try:
   
    browser = webdriver.Chrome()
    browser.get(link)
    x_element1 = browser.find_element(By.ID, "num1")
    num1 = x_element1.text

    x_element2 = browser.find_element(By.ID, "num2")
    num2 = x_element2.text
    y = str(int(num1) + int(num2))
   
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y) # ищем элемент с текстом "Python"

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла