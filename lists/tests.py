from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_first(self):
        self.browser.get('http://localhost:8500')

        self.assertIn('Cat', self.browser.title)