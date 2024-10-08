from datetime import datetime
from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def new_user_email():
    data = datetime.now()
    email = f'RuslanAb14{int(datetime.timestamp(data))}@yandex.ru'
    return email

@pytest.fixture
def autorised_user_email():
    email = f'RuslanAb140@yandex.ru'
    return email
