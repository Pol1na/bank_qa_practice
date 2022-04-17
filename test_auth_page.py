import pytest

import utils
from pages.login_page import LoginPage

link = 'https://www.demo.guru99.com/V4/'


class TestAuthPage:
    def test_user_cant_see_labels(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_not_be_labels()

    def test_user_must_see_labels(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_labels()

    @pytest.mark.parametrize(
        'login,password', [(utils.PASSWORD, utils.LOGIN),
                           (utils.WRONG_LOGIN, utils.PASSWORD),
                           (utils.WRONG_LOGIN, utils.PASSWORD),
                           (utils.LOGIN, utils.WRONG_PASSWORD)])
    def test_user_must_not_auth(self, browser, login, password):
        page = LoginPage(browser, link)
        page.open()
        page.user_incorrect_authorization(login, password)

    def test_user_auth(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.user_authorization()

    def test_correct_manager_id(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.user_authorization()
        page.manager_correct_id()
        page.manager_correct_title()
