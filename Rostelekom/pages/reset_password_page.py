from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class ResetPasswordPage(BasePage):
    LOGIN_WITH_PASS = (By.ID, 'standard_auth_btn')  # Кнопка "Войти со своим паролем"
    FORGOT_PASSWORD = (By.ID, 'forgot_password') #Кнопка "Забыл пароль"
    LOGIN_INPUT = (By.ID, 'username')  # Поле ввода номера/логина/почты/лицевого счета
    BTN_NUMBER = (By.ID, "t-btn-tab-phone") #Кнопка выбора раздела "Номер" при авторизации
    BTN_MAIL = (By.ID, "t-btn-tab-mail") #Кнопка выбора раздела "Почта" при авторизации
    BTN_LOGIN = (By.ID, "t-btn-tab-login") #Кнопка выбора раздела "Логин" при авторизации
    BTN_LS = (By.ID, "t-btn-tab-ls") #Кнопка выбора раздела "Лицевой счет" при авторизации
    BUTTON_RESET = (By.ID, "reset") #Кнопка "Продолжить"

    def reset_password_with_number(self, number):
        self.click(self.LOGIN_WITH_PASS)
        self.click(self.FORGOT_PASSWORD)
        self.click(self.BTN_NUMBER)
        self.enter_text(self.LOGIN_INPUT, number)
        time.sleep(20) #Время для ручного ввода капчи
        self.click(self.BUTTON_RESET)

    def reset_password_with_email(self, mail):
        self.click(self.LOGIN_WITH_PASS)
        self.click(self.FORGOT_PASSWORD)
        self.click(self.BTN_MAIL)
        self.enter_text(self.LOGIN_INPUT, mail)
        time.sleep(20) #Время для ручного ввода капчи
        self.click(self.BUTTON_RESET)

    def reset_password_with_login(self, login):
        self.click(self.LOGIN_WITH_PASS)
        self.click(self.FORGOT_PASSWORD)
        self.click(self.BTN_LOGIN)
        self.enter_text(self.LOGIN_INPUT, login)
        time.sleep(20) #Время для ручного ввода капчи
        self.click(self.BUTTON_RESET)

    def reset_password_with_ls(self, ls):
        self.click(self.LOGIN_WITH_PASS)
        self.click(self.FORGOT_PASSWORD)
        self.click(self.BTN_LS)
        self.enter_text(self.LOGIN_INPUT, ls)
        time.sleep(20) #Время для ручного ввода капчи
        self.click(self.BUTTON_RESET)