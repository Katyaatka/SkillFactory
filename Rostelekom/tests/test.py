import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from pages.sign_up_page import SignUp
from pages.login_time_code_page import LoginTimeCodePage
import os
from dotenv import load_dotenv
load_dotenv()

mail = os.getenv("mail")
password = os.getenv("password")
number = os.getenv("number")
ls = os.getenv("ls")
name = os.getenv("name")
last_name = os.getenv("last_name")
password_confirm = os.getenv("password_confirm")
login = os.getenv("login")

@pytest.mark.skip(reason="Тест условный, номер взять случайный")
def test_login_by_number(browser):
    '''Проверка наличия капчи на странице, которая открывается после авторизации с валидными данными
    по номеру телефона'''

    page = LoginPage(browser)
    page.login_by_number(number, password)
    elem = browser.find_element(By.CLASS_NAME, "app-header_profile_header_user")

    assert elem.is_displayed()


def test_login_by_mail(browser):
    '''Проверка наличия капчи на странице, которая открывается после авторизации с валидными данными
    по электронной почте. Используется временный почтовый ящик'''

    page = LoginPage(browser)
    page.login_by_mail(mail, password)
    elem = browser.find_element(By.CLASS_NAME, "app-header_profile_header_user")

    assert elem.is_displayed()

@pytest.mark.skip(reason="Тест условный, логин взять случайный")
def test_login_by_number(browser):
    '''Проверка наличия капчи на странице, которая открывается после авторизации с валидными данными
    по номеру телефона'''

    page = LoginPage(browser)
    page.login_by_number(number, password)
    elem = browser.find_element(By.CLASS_NAME, "app-header_profile_header_user")

    assert elem.is_displayed()

@pytest.mark.skip(reason="Тест условный, лицевой счет взять случайный")
def test_login_by_ls(browser):
    '''Проверка наличия капчи на странице, которая открывается после авторизации с валидными данными
    по лицевому счету'''

    page = LoginPage(browser)
    page.login_by_ls(ls, password)
    elem = browser.find_element(By.CLASS_NAME, "app-header_profile_header_user")

    assert elem.is_displayed()


def test_sign_up_with_email(browser):
    '''Проверка наличия капчи на странице, которая открывается после регистрации пользователя через
    почту (В методе используется ожидание для ручного выбора региона). Используется временный почтовый адрес'''

    page = SignUp(browser)
    page.sign_up_with_email(name, last_name, mail, password)
    elem = browser.find_element(By.NAME, "captcha")

    assert elem.is_displayed()

@pytest.mark.skip(reason="Тест условный, номер взять случайный")
def test_sign_up_with_number(browser):
    '''Проверка наличия капчи на странице, которая открывается после регистрации пользователя через
    номер телефона (В методе используется ожидание для ручного выбора региона)'''

    page = SignUp(browser)
    page.sign_up_with_email(name, last_name, number, password)
    elem = browser.find_element(By.NAME, "captcha")

    assert elem.is_displayed()

def test_login_time_code_with_email(browser):
    '''Проверка наличия поля для ввода временного кода на странице, которая открывается после введения почты
    и перехода на страницу для ввода кода. Используется временный почтовый ящик'''

    page = LoginTimeCodePage(browser)
    page.get_code_with_email(mail)
    elem = browser.find_element(By.ID, "captcha")

    assert elem.is_displayed()

@pytest.mark.skip(reason="Тест условный, номер взять случайный")
def test_login_time_code_with_number(browser):
    '''Проверка наличия поля для ввода временного кода на странице, которая открывается после введения номера телефона
    и перехода на страницу для ввода кода'''

    page = LoginTimeCodePage(browser)
    page.get_code_with_number(number)
    elem = browser.find_element(By.ID, "captcha")

    assert elem.is_displayed()

@pytest.mark.skip(reason="Тест условный, номер взять случайный")
def test_reset_password_with_number(browser):
    '''Проверка наличия поля для ввода кода подтверждения на странице, которая открывается послее введения номера
    телефона и капчи'''

    page = ResetPasswordPage(browser)
    page.reset_password_with_number(number)
    elem = browser.find_element(By.ID, "captcha")

    assert elem.is_displayed()

def test_reset_password_with_email(browser):
    '''Проверка наличия поля для ввода кода подтверждения на странице, которая открывается послее введения почты
     и капчи. Используется временный почтовый адрес'''

    page = ResetPasswordPage(browser)
    page.reset_password_with_email(mail)
    elem = browser.find_element(By.ID, "captcha")

    assert elem.is_displayed()

@pytest.mark.skip(reason = "Тест условный, логин подобран случайно")
def test_reset_password_with_login(browser):
    '''Проверка наличия поля для ввода кода подтверждения на странице, которая открывается послее введения логина
     и капчи'''

    page = ResetPasswordPage(browser)
    page.reset_password_with_login(login)
    elem = browser.find_element(By.ID, "captcha")

    assert elem.is_displayed()

@pytest.mark.skip(reason = "Тест условный, лицевой счет подобран случайно")
def test_reset_password_with_ls(browser):
    '''Проверка наличия поля для ввода кода подтверждения на странице, которая открывается послее введения лицевого
    счета и капчи'''

    page = ResetPasswordPage(browser)
    page.reset_password_with_ls(ls)
    elem = browser.find_element(By.ID, "captcha")

    assert elem.is_displayed()

def test_sign_up_with_email_and_different_passwords(browser):
    '''Негативный тест. Проверка возникновения ошибки "Пароли не совпадают" при регистрации через почту и вводе разных
    паролей в поля "Новый пароль" и "Подтверждение пароля". Используется временный почтовый адрес'''

    page = SignUp(browser)
    page.sign_up_with_email_and_different_passwords(name, last_name, mail, password, password_confirm)
    elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Пароли не совпадают')]")))

    assert elem.is_displayed(), 'Ошибка не возникает'

@pytest.mark.skip(reason="Тест условный, номер взять случайный")
def test_sign_up_with_number_and_different_passwords(browser):
    '''Негативный тест. Проверка возникновения ошибки "Пароли не совпадают" при регистрации через номер телефона и вводе
     разных паролей в поля "Новый пароль" и "Подтверждение пароля"'''

    page = SignUp(browser)
    page.sign_up_with_email_and_different_passwords(name, last_name, mail, password, password_confirm)
    elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Пароли не совпадают')]")))

    assert elem.is_displayed(), 'Ошибка не возникает'


@pytest.mark.parametrize('mails',
                         ['', 'grr4x@tiffincrane', 'grr4xtiffincrane.com'],
                         ids=[
                             'пустая строка',
                             'почта без домена',
                             'почта без @'
                         ]
                         )
@pytest.mark.parametrize('passwords',
                         ['', 'Ab1234!', 'abcd12345!', '1ж34567890', 'ABCDEabcde1234567890!'],
                         ids=[
                             'пустая строка',
                             '7 символов',
                             'без заглавной',
                             'без латинских символов',
                             '21 символ'
                         ]
                         )
def test_sign_up_with_email_negative(browser, mails, passwords):
    '''Негативный тест. Проверка возникновения ошибок при использовании различных комбинаций почты и пароля.
    Использованы техники тест-дизайна: граничные значения (7 и 21 символы пароля), эквивалентное разбиение (пустые
     строки у почты и у пароля). Также используется параметризация, чтобы протестировать возможные варианты с
     невалидными тестовыми данными'''

    page = SignUp(browser)
    page.sign_up_with_email_and_params(name, last_name, mails, passwords)
    wait = WebDriverWait(browser, 10)

    elem_one = wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//span[contains(@class,'rt-input-container__meta--error') and contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru')]"
    )))

    elem_two = wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//span[contains(@class,'rt-input-container__meta--error') and contains(text(),'Пароль должен содержать хотя бы одну заглавную букву')]"
    )))

    elem_three = wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//span[contains(@class,'rt-input-container__meta--error') and contains(text(),'Длина пароля должна быть не менее 8 символов')]"
    )))

    elem_four = wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//span[contains(@class,'rt-input-container__meta--error') and contains(text(),'Пароль должен содержать только латинские буквы')]"
    )))

    elem_five = wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//span[contains(@class,'rt-input-container__meta--error') and contains(text(),'Длина пароля должна быть не более 20 символов')]"
    )))

    assert (elem_one and elem_one[0].is_displayed()) or \
           (elem_two and elem_two[0].is_displayed()) or \
           (elem_three and elem_three[0].is_displayed()) or \
           (elem_four and elem_four[0].is_displayed()) or \
           (elem_five and elem_five[0].is_displayed()), "Ожидаемые ошибки не найдены"