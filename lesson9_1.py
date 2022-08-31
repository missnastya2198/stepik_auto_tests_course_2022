from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
   
    browser = webdriver.Chrome()
    browser.get(link)
    sub = browser.find_element(By.TAG_NAME, "button")
    #sub = browser.find_element(By.XPATH, "//button[@type='submit']")
    sub.click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0] #имя текущей вкладки, чтобы иметь возможность потом к ней вернуться
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print(browser.switch_to.alert.text) #вывести ответ с алерта в консоль



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла