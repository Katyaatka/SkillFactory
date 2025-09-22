from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class SignUp(BasePage):

    LOGIN_WITH_PASS = (By.ID, 'standard_auth_btn') #Кнопка "Войти со своим паролем"
    SIGN_UP = (By.ID, "kc-register") #Кнопка "зарегистрироваться"
    NAME_INPUT = (By.NAME, 'firstName') #Поле "Имя"
    LAST_NAME_INPUT = (By.NAME, 'lastName') #Поле "Фамилия"
    EMAIL_OR_NUMBER_INPUT = (By.ID, 'address') #Поле "E-mail или номер телефона"
    PASSWORD_INPUT = (By.ID, 'password') #Поле "Пароль"
    PASSWORD_CONFIRM_INPUT = (By.ID, 'password-confirm') #Поле "Подтверждение пароля"
    SIGN_UP_BUTTON = (By.NAME, 'register') #Кнопка "Зарегистрироваться"


    def sign_up_with_email(self, name, last_name, email, password):
        '''Метод для регистрации пользователя через почту. В метод может передаваться как почта, так
        и номер телефона для регистрации пользователя'''

        self.click(self.LOGIN_WITH_PASS)
        self.click(self.SIGN_UP)
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.EMAIL_OR_NUMBER_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.enter_text(self.PASSWORD_CONFIRM_INPUT, password)
        time.sleep(5) #Время для ручного выбора региона
        self.click(self.SIGN_UP_BUTTON)


    def sign_up_with_number(self, name, last_name, number, password):
        '''Метод для регистрации пользователя через номер телефона. В метод может передаваться как почта, так
        и номер телефона для регистрации пользователя'''

        self.click(self.LOGIN_WITH_PASS)
        self.click(self.SIGN_UP)
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.EMAIL_OR_NUMBER_INPUT, number)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.enter_text(self.PASSWORD_CONFIRM_INPUT, password)
        time.sleep(5) #Время для ручного выбора региона
        self.click(self.SIGN_UP_BUTTON)

    def sign_up_with_email_and_different_passwords(self, name, last_name, email, password, password_confirm):
        '''Метод для регистрации пользователя через почту с разными паролями в поля "Новый пароль" и "Подтверждение
        пароля"'''

        self.click(self.LOGIN_WITH_PASS)
        self.click(self.SIGN_UP)
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.EMAIL_OR_NUMBER_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.enter_text(self.PASSWORD_CONFIRM_INPUT, password_confirm)
        time.sleep(5) #Время для ручного выбора региона
        self.click(self.SIGN_UP_BUTTON)


    def sign_up_with_number_and_different_passwords(self, name, last_name, number, password, password_confirm):
        '''Метод для регистрации пользователя через номер телефона с разными паролями в поля "Новый пароль" и "Подтверждение
        пароля"'''

        self.click(self.LOGIN_WITH_PASS)
        self.click(self.SIGN_UP)
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.EMAIL_OR_NUMBER_INPUT, number)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.enter_text(self.PASSWORD_CONFIRM_INPUT, password_confirm)
        time.sleep(5) #Время для ручного выбора региона
        self.click(self.SIGN_UP_BUTTON)

    def sign_up_with_email_and_params(self, name, last_name, mails, passwords):
        '''Метод для регистрации пользователя через почту с использованием различных комбинаций логинов и паролей'''

        self.click(self.LOGIN_WITH_PASS)
        self.click(self.SIGN_UP)
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.EMAIL_OR_NUMBER_INPUT, mails)
        self.enter_text(self.PASSWORD_INPUT, passwords)
        self.enter_text(self.PASSWORD_CONFIRM_INPUT, passwords)
        time.sleep(5) #Время для ручного выбора региона
        self.click(self.SIGN_UP_BUTTON)

    def sign_up_with_number_and_params(self, name, last_name, numbers, passwords):
        '''Метод для регистрации пользователя через почту с использованием различных комбинаций логинов и паролей'''

        self.click(self.LOGIN_WITH_PASS)
        self.click(self.SIGN_UP)
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.EMAIL_OR_NUMBER_INPUT, numbers)
        self.enter_text(self.PASSWORD_INPUT, passwords)
        self.enter_text(self.PASSWORD_CONFIRM_INPUT, passwords)
        time.sleep(5) #Время для ручного выбора региона
        self.click(self.SIGN_UP_BUTTON)