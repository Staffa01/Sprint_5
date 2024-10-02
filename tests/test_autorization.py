import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
# import lokator
from ..lokator import lokator

def test_auth_with_button_enter_akount(autorised_user_email):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, lokator.enter_in_akount_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, lokator.email_input)))
    element = driver.find_element(By.XPATH, lokator.email_input)
    element.send_keys(autorised_user_email)
    element = driver.find_element(By.NAME, 'Пароль')
    element.send_keys("qwerty")
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, lokator.enter_button)))
    element = driver.find_element(By.XPATH, lokator.enter_button)
    print(element)
    element.click()
    # time.sleep(10)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
    time.sleep(10)
    assert driver.find_element(By.XPATH, lokator.place_an_order_buton).text == "Оформить заказ"
    driver.quit()


def test_auth_with_button_profile(autorised_user_email):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.quit()