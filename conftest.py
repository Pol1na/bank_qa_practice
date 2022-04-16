import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose your browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru', help='Choose lang: ru/en/es etc')


@pytest.fixture
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print(f'starting chrome. Language: {user_language}')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        print(f'starting firefox. Language: {user_language}')
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print('quit browser')
    browser.quit()
