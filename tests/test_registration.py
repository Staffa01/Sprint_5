from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ..locators_xpath import Lokator


class TestRegistration:
    def test_registration_confirm(self, driver, new_user_email):
        driver.get(Lokator.url['base'])
        driver.find_element(By.XPATH, Lokator.enter_in_akount_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.registration_link)))
        driver.find_element(By.XPATH, Lokator.registration_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.registration_buton)))
        elements = driver.find_elements(By.NAME, "name")
        elements[0].send_keys("Ruslan")
        elements[1].send_keys(new_user_email)
        driver.find_element(By.NAME,'Пароль').send_keys("qwerty")
        driver.find_element(By.XPATH, Lokator.registration_buton).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,Lokator.enter_button)))
        elements= driver.find_elements(By.XPATH, Lokator.email_input)
        elements[0].send_keys(new_user_email)
        driver.find_element(By.NAME, 'Пароль').send_keys("qwerty")
        element = driver.find_element(By.XPATH, Lokator.enter_button)
        element.click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Lokator.place_an_order_buton)))
        assert driver.find_element(By.XPATH, Lokator.place_an_order_buton).text == "Оформить заказ"



    def test_registration_with_invalid_password_not_registred(self, driver, new_user_email):
        driver.get(Lokator.url['base'])
        driver.find_element(By.XPATH, Lokator.enter_in_akount_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.registration_link)))
        driver.find_element(By.XPATH, Lokator.registration_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.registration_buton)))
        elements = driver.find_elements(By.NAME, "name")
        elements[0].send_keys("Ruslan")
        elements[1].send_keys(new_user_email)
        driver.find_element(By.NAME, 'Пароль').send_keys("qw")
        driver.find_element(By.XPATH, Lokator.registration_buton).click()
        assert driver.find_element(By.XPATH,Lokator.wrong_password).text == 'Некорректный пароль'


