from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@label="Войти"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON_QR = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    RESTORE_LINK = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    REGISTRATION_BUTTON = (By.XPATH, '//span[text()="Зарегистрироваться"]')
    LOGIN_BUTTON_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_BUTTON_MAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_BUTTON_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[text()="Введите логин" or text()="Введите пароль"]')
    RECOVER_ACCOUNT = (By.XPATH, '//span[text()="Восстановить"]')
    GO_BACK_BUTTON = (By.XPATH, '//span[text()="Отмена"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_QR)
        self.find_element(LoginPageLocators.RESTORE_LINK)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_VK)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_MAIL)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_YANDEX)

    @allure.step('Вводим логин')
    def login_entry(self, LOGIN):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(LOGIN)
        self.attach_screenshot()


    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()


    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Заполняем поле пароль')
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RECOVER_ACCOUNT).click()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()

