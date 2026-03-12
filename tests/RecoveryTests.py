import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper

BASE_URL = 'https://ok.ru/'
LOGIN = 'test@gmail.com'
PASSWORD = '1'

@allure.suite('Проверка восстановления пользователя')
@allure.step('Проверка перехода к восстановлению после нескольких неудачных попыток авторизации')
def test_go_to_recovery_after_many_fails(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.login_entry(LOGIN)

    for i in range(3):
        LoginPage.type_password(PASSWORD)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelper(browser)