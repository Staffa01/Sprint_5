import json
import pytest
import random

def read_test_data():
    file = open('../test_data.txt', 'r')
    data_dict = json.load(file)
    file.close()
    return data_dict


def write_test_data(data_dict):
    file = open('../test_data.txt', 'w')
    json.dump(data_dict, file)
    file.close()


@pytest.fixture
def new_user_email():
    data_dict = read_test_data()
    index = int(data_dict['user_index'])
    email = f'RuslanAb14{index}@yandex.ru'
    return email


@pytest.fixture
def autorised_user_email():
    data_dict = read_test_data()
    index = random.randint(0, int(data_dict['user_index'])-1)
    email = f'RuslanAb14{index}@yandex.ru'
    return email
