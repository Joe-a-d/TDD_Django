from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()


    # helpers

    def check_li_created(self, item_text):
        # for long loads keep trying and execute until up to 10s
        start_time = time.time()
        while True:
            try:
                list = self.browser.find_element_by_id('list_general')
                list_items = list.find_elements_by_tag_name("li")
                self.assertIn(item_text, [item_text for item in list_items])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_create_and_get_list(self):
        # Mike access the homepage
        self.browser.get(self.live_server_url)

        # He notices that the tab and the page's header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        # He's immediately prompted to create an to-do item
        inputbox = self.browser.find_element_by_id('new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Add a task')

        # He types 'meditate for 20min' into a textbox
        item_text = 'meditate for 20min'
        inputbox.send_keys(item_text)

        # When he hits enter the form is sent and the page updates showing his task in an ordered list
        inputbox.send_keys(Keys.ENTER)

        self.check_li_created(item_text)
        
        # The inputbox is still there. He adds another item which reads "clean gutters"
        item_text2 = 'clean gutters'
        inputbox = self.browser.find_element_by_id('new_item')
        inputbox.click()
        inputbox.send_keys(item_text2)
        inputbox.send_keys(Keys.ENTER)

        # The page updates again showing the two items
        self.check_li_created(item_text)
        self.check_li_created(item_text2)


    def test_unique_url_per_user(self):
        # Mike starts a list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('new_item')
        inputbox.send_keys('meditate for 20min')
        inputbox.send_keys(Keys.ENTER)
        self.check_li_created('medidate for 20min')

        # he sees that a unique URL to his list has been created

        mike_list_url = self.browser.current_url
        ## matches against regex
        self.assertRegex(mike_list_url, '/lists/.+')

        # loretta logins in from her laptop 

        ## new session
        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url)

        # and can't see Mike's list
        body = self.browser.find_element_by_tag_name('body')
        self.assertNotIn('meditate for 20min', body.text)
        self.assertNotIn('clean gutters', body.text)

        # loretta starts a new list and adds 'buy milk' to it

        inputbox = self.browser.find_element_by_id('new_item')
        inputbox.send_keys('buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_li_created('buy milk')

        # she gets the unique url which links to ther list

        lor_list_url = self.browser.current_url
        self.assertRegex(lor_list_url, '/lists/.+')
        self.assertNotEqual(mike_list_url, lor_list_url)


