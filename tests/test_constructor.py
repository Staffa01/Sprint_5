import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lokators import Lokator

def test_constructor_chapter_fillings():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Lokator.span_fillings)))
    driver.find_element(By.XPATH, Lokator.span_fillings).click()
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//img[@alt='Мясо бессмертных моллюсков Protostomia']")))
    driver.quit()

def test_constructor_chapter_sauces():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Lokator.span_sauces)))
    driver.find_element(By.XPATH, Lokator.span_sauces).click()
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//img[@alt='Соус Spicy-X']")))
    driver.quit()

def test_constructor_chapter_buns():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Lokator.span_buns)))
    driver.find_element(By.XPATH, Lokator.span_fillings).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//img[@alt='Мясо бессмертных моллюсков Protostomia']")))
    driver.find_element(By.XPATH, Lokator.span_buns).click()
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")))
    driver.quit()