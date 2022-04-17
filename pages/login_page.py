import time

from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import utils
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):

    def should_not_be_labels(self):
        self.is_not_element_presented(*LoginPageLocators.LABEL_LOGIN)
        self.is_not_element_presented(*LoginPageLocators.LABEL_PASSWORD)

    def should_be_labels(self):
        self.browser.find_element(*LoginPageLocators.INPUT_LOGIN).click()
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).click()
        self.is_element_present(*LoginPageLocators.LABEL_LOGIN)
        self.browser.find_element(*LoginPageLocators.INPUT_LOGIN).click()
        self.is_element_present(*LoginPageLocators.LABEL_PASSWORD)

    def user_authorization(self):
        self.browser.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(utils.LOGIN)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(utils.PASSWORD)
        self.should_not_be_labels()
        self.browser.find_element(*LoginPageLocators.AUTH_BTN).click()
        assert self.browser.find_element(*MainPageLocators.TEXT_TITLE).text == 'Guru99 Bank', 'Wrong title'

    def user_incorrect_authorization(self, login=utils.WRONG_LOGIN, password=utils.WRONG_PASSWORD):
        self.browser.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(login)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(password)
        self.should_not_be_labels()
        self.browser.find_element(*LoginPageLocators.AUTH_BTN).click()
        assert self.browser.switch_to.alert.text == LoginPageLocators.MESSAGE_WRONG_CREDENTIALS, "No error message"

    def manager_correct_id(self):
        assert self.browser.find_element(*MainPageLocators.WELCOME_TITLE).text.split(': ')[
                   1] == utils.LOGIN, 'Incorrect ID'

    def manager_correct_title(self):
        assert self.browser.find_element(*MainPageLocators.WELCOME_TITLE).text == "Manager Id : mngr399216", 'Bad text'
