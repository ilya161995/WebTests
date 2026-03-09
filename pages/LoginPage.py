from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@label="Войти"]')
    LOGIN_PASSWORD = (By.ID, 'field_password')
    LOGIN_BUTTON_QR = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    RESTORE_LINK = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    REGISTRATION_BUTTON = (By.XPATH, '//span[text()="Зарегистрироваться"]')
    LOGIN_BUTTON_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_BUTTON_MAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_BUTTON_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[text()="Введите логин" or text()="Введите пароль"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_PASSWORD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_QR)
        self.find_element(LoginPageLocators.RESTORE_LINK)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_VK)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_MAIL)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_YANDEX)

    def login_entry(self, LOGIN):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(LOGIN)


    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()


    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text