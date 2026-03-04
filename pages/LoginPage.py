from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[1]/form/button/span')
    LOGIN_PASSWORD = (By.ID, 'field_password')
    LOGIN_BUTTON_QR = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[1]/button/span')
    LOGIN_BUTTON_1 = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[1]/span/button')
    LOGIN_BUTTON_2 = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[3]/button/span')
    LOGIN_BUTTON_VK = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[1]/i')
    LOGIN_BUTTON_MAIL = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[1]/i')
    LOGIN_BUTTON_YANDEX = (By.XPATH, '//*[@id="tabpanel-login-2075072712"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[3]/i')


class LoginPageHelper(BasePage):
    pass