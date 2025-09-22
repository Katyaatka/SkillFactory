from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):


    LOGIN_WITH_PASS = (By.ID, 'standard_auth_btn') #Кнопка "Войти со своим паролем"
    LOGIN_INPUT = (By.ID, 'username') #Поле ввода номера/логина/почты/лицевого счета
    PASSWORD_INPUT = (By.ID, 'password') #Поле ввода пароля
    BTN_NUMBER = (By.ID, "t-btn-tab-phone") #Кнопка выбора раздела "Номер" при авторизации
    BTN_MAIL = (By.ID, "t-btn-tab-mail") #Кнопка выбора раздела "Почта" при авторизации
    BTN_LOGIN = (By.ID, "t-btn-tab-login") #Кнопка выбора раздела "Логин" при авторизации
    BTN_LS = (By.ID, "t-btn-tab-ls") #Кнопка выбора раздела "Лицевой счет" при авторизации
    BUTTON_LOGIN = (By.ID, 'kc-login') #Кнопка "Войти"

    def login_by_number(self, number, password):
        '''Метод для ввода номера телефона, пароля и авторизации пользователя'''

        self.click(self.LOGIN_WITH_PASS)
        self.click(self.BTN_NUMBER)
        self.enter_text(self.LOGIN_INPUT, number)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.BUTTON_LOGIN)

    def login_by_mail(self, mail, password):
        '''Метод для ввода почты, пароля и авторизации пользователя'''

        self.click(self.LOGIN_WITH_PASS)
        self.click(self.BTN_MAIL)
        self.enter_text(self.LOGIN_INPUT, mail)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.BUTTON_LOGIN)

    def login_by_login(self, login, password):
        '''Метод для ввода логина, пароля и авторизации пользователя'''

        self.click(self.LOGIN_WITH_PASS)
        self.click(self.BTN_LOGIN)
        self.enter_text(self.LOGIN_INPUT, login)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.BUTTON_LOGIN)

    def login_by_ls(self, ls, password):
        '''Метод для ввода лицевого счета, пароля и авторизации пользователя'''

        self.click(self.LOGIN_WITH_PASS)
        self.click(self.BTN_LS)
        self.enter_text(self.LOGIN_INPUT, ls)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.BUTTON_LOGIN)