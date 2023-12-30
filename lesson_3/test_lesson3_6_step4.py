import pytest
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize('index', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_login(browser, index):
    try:
        link = f"https://stepik.org/lesson/{index}/step/1"
        browser.get(link)

        time.sleep(10)

        login_btn = browser.find_element(By.XPATH, '//*[text()="Войти"]')
        login_btn.click()

        login_input = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
        login_input.send_keys("htyrmd@gmail.com")

        pass_input = browser.find_element(By.XPATH, '//*[@id="id_login_password"]')
        pass_input.send_keys("39Vn_x2G8o_uR93")
        pass_input.send_keys(Keys.ENTER)

        time.sleep(10)
        
        answer = math.log(int(time.time()))

        answer_input = browser.find_element(By.XPATH, '//*[@Placeholder="Напишите ваш ответ здесь..."]')
        answer_input.send_keys(answer)

        send_button = browser.find_element(By.XPATH, '//*[text()="Отправить"]')
        send_button.click()

        optional_response1 = browser.find_element(By.CLASS_NAME, 'attempt-message_correct')
        assert "Здорово, всё верно." == optional_response1.get_attribute("Text")

        optional_response2 = browser.find_element(By.CLASS_NAME, 'smart-hints.ember-view.lesson__hint')
        assert "Correct!" == optional_response2.get_attribute("Text")

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(25)