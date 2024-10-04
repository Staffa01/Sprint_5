import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lokators import Lokator

def test_transition_to_profile(autorised_user_email):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, Lokator.profile_button_header).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.email_input)))
    driver.find_element(By.XPATH, Lokator.email_input).send_keys(autorised_user_email)
    element = driver.find_element(By.NAME, 'Пароль')
    element.send_keys("qwerty")
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.enter_button)))
    driver.find_element(By.XPATH, Lokator.enter_button).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Lokator.place_an_order_buton)))
    driver.find_element(By.XPATH, Lokator.profile_button_header).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Lokator.order_history)))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
    driver.quit()

def test_transition_to_constructor_into_profile(autorised_user_email):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, Lokator.profile_button_header).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.email_input)))
    driver.find_element(By.XPATH, Lokator.email_input).send_keys(autorised_user_email)
    element = driver.find_element(By.NAME, 'Пароль')
    element.send_keys("qwerty")
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.enter_button)))
    driver.find_element(By.XPATH, Lokator.enter_button).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Lokator.place_an_order_buton)))
    driver.find_element(By.XPATH, Lokator.profile_button_header).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Lokator.order_history)))
    driver.find_element(By.XPATH, Lokator.stellar_burgers_logo).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Lokator.place_an_order_buton)))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()