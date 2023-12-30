from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)

    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button0 = browser.find_element(By.XPATH, '//*[text()="Book"]')
    button0.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button1 = browser.find_element(By.XPATH, '//*[text()="Submit"]')
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла