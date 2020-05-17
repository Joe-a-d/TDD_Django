from selenium import webdriver
import unittest

## UserStory 

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # run when instantiating NewVisitorTest
        self.browser = webdriver.Firefox()

    def tearDown(self):
        # run just before destorying NewVisitorTest
        self.browser.quit()

    def test_first(self):
        ## User A access the website
        self.browser.get('http://localhost:8500')

        ## she notices that the tab and the header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('End Test')

# launch test runner if ran from terminal
if __name__ == '__main__':
    unittest.main()