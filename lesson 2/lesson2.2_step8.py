from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os 

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//*[@placeholder="Enter first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//*[@placeholder="Enter last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//*[@placeholder="Enter email"]')
    input3.send_keys("test@test.test")
    input4 = browser.find_element(By.XPATH, '//*[@id="file"]')
    input4.send_keys(file_path)
    button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла