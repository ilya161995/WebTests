from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-243955410"]/vkid-form-adapter/div/div/div/div[1]/form/button')
    LOGIN_PASSWORD = (By.ID, 'field_password')
    LOGIN_BUTTON_QR = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[1]/button/span')
    LOGIN_BUTTON_1 = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[1]/span/button')
    LOGIN_BUTTON_2 = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[3]/button/span')
    LOGIN_BUTTON_VK = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[1]/i')
    LOGIN_BUTTON_MAIL = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[1]/i')
    LOGIN_BUTTON_YANDEX = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[3]/i')
    ERROR_TEXT = (By.XPATH, '//*[@id="tabpanel-login-5565835368"]/vkid-form-adapter/div/div/div/div[1]/form/div[2]/span[2]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_PASSWORD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_QR)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_1)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_2)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_VK)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_MAIL)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_YANDEX)

    def login_entry(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys()


    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()


    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text