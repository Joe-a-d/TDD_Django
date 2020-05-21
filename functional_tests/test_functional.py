from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time

class NewVisitorTest(LiveServerTestCase):


	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()


	# helpers

	def check_li_created(self, item_text):
		list = self.browser.find_element_by_id('list_general')
		list_items = list.find_elements_by_tag_name("li")
		self.assertIn(item_text, [item.text for item in list_items])

	def test_create_and_get_list(self):
		# Mike access the homepage
		self.browser.get("http://127.0.0.1:8000")

		# He notices that the tab and the page's header mention to-do lists
		self.assertIn("To-Do", self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn("To-Do", header_text)

		# He's immediately prompted to create an to-do item
		inputbox = self.browser.find_element_by_id('new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Add a task')

		# He types 'meditate for 20min' into a textbox
		item_text = 'meditate for 20min'
		text_input = inputbox.send_keys(item_text)

		# When he hits enter the form is sent and the page updates showing his task in an ordered list
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		self.check_li_created(item_text)
		
		# The inputbox is still there. He adds another item which reads "clean gutters"

		# The page updates again showing the two items