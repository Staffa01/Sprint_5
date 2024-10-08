from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ..locators_xpath import Lokator

class TestAutorization:
    def test_auth_with_button_enter_akount(self, driver, autorised_user_email):
        driver.get(Lokator.url['base'])
        driver.find_element(By.XPATH, Lokator.enter_in_akount_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.email_input)))
        element = driver.find_element(By.XPATH, Lokator.email_input)
        element.send_keys(autorised_user_email)
        element = driver.find_element(By.NAME, 'Пароль')
        element.send_keys("qwerty")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.enter_button)))
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Lokator.enter_button)))
        driver.find_element(By.XPATH, Lokator.enter_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.enter_button)))
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Lokator.place_an_order_buton)))
        assert driver.find_element(By.XPATH, Lokator.place_an_order_buton).text == "Оформить заказ"
        driver.quit()


    def test_auth_with_button_profile(self, driver, autorised_user_email):
        driver.get(Lokator.url['base'])
        driver.find_element(By.XPATH, Lokator.profile_button_header).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.email_input)))
        element = driver.find_element(By.XPATH, Lokator.email_input)
        element.send_keys(autorised_user_email)
        element = driver.find_element(By.NAME, 'Пароль')
        element.send_keys("qwerty")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.enter_button)))
        element = driver.find_element(By.XPATH, Lokator.enter_button)
        element.click()
        WebDriverWait(driver, 10).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, Lokator.place_an_order_buton)))
        assert driver.find_element(By.XPATH, Lokator.place_an_order_buton).text == "Оформить заказ"

    def test_auth_with_registration_form(self, driver, autorised_user_email):
        driver.get(Lokator.url['login'])
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.email_input)))
        element = driver.find_element(By.XPATH, Lokator.email_input)
        element.send_keys(autorised_user_email)
        element = driver.find_element(By.NAME, 'Пароль')
        element.send_keys("qwerty")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.enter_button)))
        element = driver.find_element(By.XPATH, Lokator.enter_button)
        element.click()
        WebDriverWait(driver, 10).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, Lokator.place_an_order_buton)))
        assert driver.find_element(By.XPATH, Lokator.place_an_order_buton).text == "Оформить заказ"

    def test_auth_with_recover_password_page(self, driver, autorised_user_email):
        driver.get(Lokator.url['forgot-password'])
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Lokator.login_button_in_recover_page)))
        driver.find_element(By.XPATH, Lokator.login_button_in_recover_page).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.email_input)))
        element = driver.find_element(By.XPATH, Lokator.email_input)
        element.send_keys(autorised_user_email)
        element = driver.find_element(By.NAME, 'Пароль')
        element.send_keys("qwerty")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Lokator.enter_button)))
        element = driver.find_element(By.XPATH, Lokator.enter_button)
        element.click()
        WebDriverWait(driver, 10).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, Lokator.place_an_order_buton)))
        assert driver.find_element(By.XPATH, Lokator.place_an_order_buton).text == "Оформить заказ"
