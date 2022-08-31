'''from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
   
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(3)
    price = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    book = browser.find_element(By.ID, "book")
    book.click()
        x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    button = browser.find_element(By.ID, "solve")
    button.click()
    print(browser.switch_to.alert.text) #вывести ответ с алерта в консоль



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла