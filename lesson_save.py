from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
'''print(os.path.abspath(os.path.dirname(__file__)))
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_path = os.path.join(current_dir, "newfile.txt")
f = open(file_path, "w")
print(f)'''

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("dmskmkcs@mail.com")
    #print(os.path.abspath(__file__))
    #print(os.path.abspath(os.path.dirname(__file__)))
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "newfile.txt") 
    f = open(file_path, "w")
    element = browser.find_element(By.ID, "file")          
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    