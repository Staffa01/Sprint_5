from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ..locators_xpath import Lokator

class TestConstructor:
    def test_constructor_chapter_fillings(self, driver, autorised_user_email):
        driver.get(Lokator.url['base'])
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Lokator.span_fillings)))
        driver.find_element(By.XPATH, Lokator.span_fillings).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Lokator.span_fillings_after_click)))


    def test_constructor_chapter_sauces(self, driver, autorised_user_email):
        driver.get(Lokator.url['base'])
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Lokator.span_sauces)))
        driver.find_element(By.XPATH, Lokator.span_sauces).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Lokator.span_sauces_after_click)))


    def test_constructor_chapter_buns(self, driver, autorised_user_email):
        driver.get(Lokator.url['base'])
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Lokator.span_sauces)))
        driver.find_element(By.XPATH, Lokator.span_sauces).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Lokator.span_buns)))
        driver.find_element(By.XPATH, Lokator.span_buns).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Lokator.span_buns_after_click)))
