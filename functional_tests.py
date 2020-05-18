from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_create_and_get_list(self):
		# Mike access the homepage
		self.browser.get("http://localhost:8000")

		# He notices that the tab and the page's header mention to-do lists
		self.assertIn("To-Do", self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn("To-Do", header_text)

		# He's immediately prompted to create an to-do item
		inputbox = self.browser.find_element_by_id('new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Add a task')

		# He types 'meditate for 20min' into a textbox
		text_input = inputbox.send_keys('meditate for 20min')

		# When he hits enter the form is sent and the page updates showing his task in an ordered list
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		list = self.browser.find_element_by_id('list_general')
		self.assertIn("1. meditate for 20min", list.find_element_by_tag_name("li"))

		# The inputbox is still there. He adds another item which reads "Clean gutters"
		self.fail("END")

		# The page updates again showing the two items

if __name__ == "__main__":
	unittest.main()

