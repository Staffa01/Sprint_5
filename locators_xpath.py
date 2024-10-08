class Lokator:
    url = {
        'base':'https://stellarburgers.nomoreparties.site/',
        'register':'https://stellarburgers.nomoreparties.site/register',
        'login':'https://stellarburgers.nomoreparties.site/login',
        'profile':'https://stellarburgers.nomoreparties.site/account/profile',
        'forgot-password':'https://stellarburgers.nomoreparties.site/forgot-password'
    }

    enter_in_akount_button = ".//button[text()='Войти в аккаунт']" #Кнопка Войти в аккаунт на главной
    registration_link = ".//a[text()='Зарегистрироваться']" #Ссылка на регистрацию в экране авторизации /login
    registration_buton = ".//button[text()='Зарегистрироваться']" #Кнопка Зарегистрироваться в экране регистрации /register
    enter_button = ".//button[text()='Войти']" #Кнопка Войти
    email_input = ".//label[text()='Email']/following::input[@name='name']" # Поле ввода почты
    password_input = ".//label[text()='Пароль']/following::input[@name='Пароль']" # Поле ввода пароля
    place_an_order_buton = ".//button[text()='Оформить заказ']" # Кнопка Оформить заказ
    profile_button_header = ".//a[contains(@href,'/account')]" # Кнопка Личный кабинет
    recover_password_link = ".//a[contains(@href,'/forgot-password')]" # Ссыдка на востановление пароля в экране авторизации /login
    recover_button = ".//button[text()='Восстановить']" # Кнопка Восстановить в экране сброса пароля /forgot-password
    login_button_in_recover_page = ".//a[contains(@href,'/login')]" #Ссылка войти в в экране восстановления пароля /reset-password
    order_history = ".//a[contains(@href,'/account/order-history')]" # Кнопка история заказов в личном профиле
    stellar_burgers_logo = ".//div[@class='AppHeader_header__logo__2D0X2']" #Кнопка stellar_burgers
    exit_button = ".//button[text()='Выход']" # Кнопка Выход в профиле
    span_fillings = ".//span[text()='Начинки']" # Разделы конструктора
    span_sauces = ".//span[text()='Соусы']"
    span_buns = ".//span[text()='Булки']"
    span_fillings_after_click = "//div[contains(@class,'tab_tab_type_current')]//span[text()='Начинки']"
    span_sauces_after_click = "//div[contains(@class,'tab_tab_type_current')]//span[text()='Соусы']"
    span_buns_after_click = "//div[contains(@class,'tab_tab_type_current')]//span[text()='Булки']"
    wrong_password = ".//div[@class='input__container']/p[text()='Некорректный пароль']"
