from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginTimeCodePage(BasePage):

    EMAIL_OR_NUMBER_INPUT = (By.ID, 'address')
    BUTTON_GET_CODE = (By.ID, 'otp_get_code')

    def get_code_with_email(self, mail):
        '''Метод для получения временного кода при отправке электронной почты на сервер'''

        self.enter_text(self.EMAIL_OR_NUMBER_INPUT, mail)
        self.click(self.BUTTON_GET_CODE)

    def get_code_with_number(self, number):
        '''Метод для получения временного кода при отправке электронной почты на сервер'''

        self.enter_text(self.EMAIL_OR_NUMBER_INPUT, number)
        self.click(self.BUTTON_GET_CODE)