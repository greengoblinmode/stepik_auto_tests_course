from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
    input2.click()
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()
    button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла