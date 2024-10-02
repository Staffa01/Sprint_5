import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from ..lokator import lokator

def test_registration_confirm(new_user_email):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, lokator.enter_in_akount_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, lokator.registration_link)))
    driver.find_element(By.XPATH, lokator.registration_link).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, lokator.registration_buton)))
    elements = driver.find_elements(By.NAME, "name")
    elements[0].send_keys("Ruslan")
    elements[1].send_keys(new_user_email)
    driver.find_element(By.NAME,'Пароль').send_keys("qwerty")
    driver.find_element(By.XPATH, lokator.registration_buton).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,lokator.enter_button)))
    elements= driver.find_elements(By.XPATH, lokator.email_input)
    # time.sleep(5)
    elements[0].send_keys(new_user_email)
    driver.find_element(By.NAME, 'Пароль').send_keys("qwerty")
    # time.sleep(1)
    element = driver.find_element(By.XPATH, lokator.enter_button)
    element.click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, lokator.place_an_order_buton)))
    assert driver.find_element(By.XPATH, lokator.place_an_order_buton).text == "Оформить заказ"
    driver.quit()

def test_registration_with_invalid_password_not_registred(new_user_email):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, lokator.enter_in_akount_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, lokator.registration_link)))
    driver.find_element(By.XPATH, lokator.registration_link).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, lokator.registration_buton)))
    elements = driver.find_elements(By.NAME, "name")
    elements[0].send_keys("Ruslan")
    elements[1].send_keys(new_user_email)
    driver.find_element(By.NAME, 'Пароль').send_keys("qw")
    driver.find_element(By.XPATH, lokator.registration_buton).click()
    assert driver.find_element(By.XPATH,".//div[@class='input__container']/p[text()='Некорректный пароль']").text == 'Некорректный пароль'
    driver.quit()

