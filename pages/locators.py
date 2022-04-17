from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_LOGIN = (By.NAME, 'uid')
    INPUT_PASSWORD = (By.NAME, 'password')
    LABEL_LOGIN = (By.ID, 'message23')
    LABEL_PASSWORD = (By.ID, 'message18')
    AUTH_BTN = (By.NAME, 'btnLogin')
    MESSAGE_WRONG_CREDENTIALS = 'User or Password is not valid'


class MainPageLocators:
    TEXT_TITLE = (By.CLASS_NAME, 'barone')
    WELCOME_TITLE = (By.CSS_SELECTOR, 'tr.heading3 > td')
