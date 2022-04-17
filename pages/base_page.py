from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class BasePage:
    def __init__(self, browser, link, timeout=4):
        #self.browser = webdriver.Chrome()
        self.browser = browser
        self.link = link
        self.timeout = timeout

    def open(self):
        self.browser.get(self.link)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_presented(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return True
        return False

