from selenium import webdriver
from testconfig import config
from termcolor import colored
import unittest


class BaseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = config['main']['url']
        self.browser = config['main']['browser']

    def setUp(self):
        # Get the home page
        self.driver = self.get_driver()
        self.driver.implicitly_wait(30)
        self.driver.get(url=self.url)

    def get_driver(self):
        # Return the webdriver
        if self.browser == 'firefox':
            return webdriver.Firefox()
        else:
            return webdriver.Chrome()

    def tearDown(self):
        # Quit the browser
        self.driver.quit()
