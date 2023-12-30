import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, '//*[@placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//*[@placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '//*[@placeholder="Input your email"]')
        input3.send_keys("test@test.test")
        input4 = browser.find_element(By.XPATH, '//*[@placeholder="Input your phone:"]')
        input4.send_keys("+79999999999")
        input5 = browser.find_element(By.XPATH, '//*[@placeholder="Input your address:"]')
        input5.send_keys("Test")

        # Отправляем заполненную форму
        button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong/No welcome text")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, '//*[@placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//*[@placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '//*[@placeholder="Input your email"]')
        input3.send_keys("test@test.test")
        input4 = browser.find_element(By.XPATH, '//*[@placeholder="Input your phone:"]')
        input4.send_keys("+79999999999")
        input5 = browser.find_element(By.XPATH, '//*[@placeholder="Input your address:"]')
        input5.send_keys("Test")

        # Отправляем заполненную форму
        button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong/No welcome text")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()