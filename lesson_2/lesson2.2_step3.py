from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)

    x = browser.find_element(By.ID, "num1")
    x = int(x.text)
    y = browser.find_element(By.ID, "num2")
    y = int(y.text)
    sum = str(x + y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)
    button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла