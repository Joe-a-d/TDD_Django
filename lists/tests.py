# Here we'll start implementing unit tests, following the TDD cycle
# 1.  Write a FT which describes some well-defined behaviour from the user's pv
# 2. Make sure that FT fails as expected and move on to writing unit tests to define how we want our code which describes that functionally to behave. Each line of production code should be tested by at least one test
# 3. Once we have a failing UT, write the smallest amount of code which gets it to past. Iterate b/ 2-3 until the likelihood of the FT passing increases.
# 4. Rerun FT test, repeat 2-3 if failing. 

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest, HttpResponse

from lists.views import home_page 
from lists.models import Item, List

class HomePageTest(TestCase):

	def test_home_template_used(self):
		# Test client is created for each test, which is accessed via the TestCase class, as oposed to client = Client() for each test

		response = self.client.get('/')

		self.assertTemplateUsed(response, 'base.html')


class NewListTest(TestCase):

	def test_POST_save(self):
		response = self.client.post('/lists/new', data={'item_text': 'meditate for 20min', })

		# check that item has been saved
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		# check content of 'text'
		self.assertEqual(new_item.text, 'meditate for 20min')

		

	def test_POST_redirect(self):

		response = self.client.post('/lists/new', data={'item_text': 'meditate for 20min'})
		new_list = List.objects.first()
		# check response for redirect
		self.assertRedirects(response, f'/lists/{new_list.id}/')


class ListViewTest(TestCase):

	def test_display_list_template_used(self):
		list_ = List.objects.create()
		response = self.client.get(f'/lists/{list_.id}/')

		self.assertTemplateUsed(response, 'display_list.html')

	def test_display_all_items(self):
		list_ = List.objects.create()
		wrong_list = List.objects.create()

		Item.objects.create(text = "item1", list=list_)
		Item.objects.create(text = "item2", list=list_)
		Item.objects.create(text = "item21", list=wrong_list)
		Item.objects.create(text = "item22", list=wrong_list)


		response = self.client.get(f'/lists/{list_.id}/')

		self.assertContains(response, "item1")
		self.assertContains(response, "item2")
		self.assertNotContains(response, "item21")
		self.assertNotContains(response, "item22")


# class NewItemTest(TestCase):

# 	# def test_save_to_existing_list(self):
# 	# 	list_ = List.objects.create()
# 	# 	wrong_list = List.objects.create()

# 	# 	self.client.post(f'/lists/{list_.id}/save_to', data={'item_text':'existing'})

# 	# 	self.assertEqual(Item.objects.count(),1)
# 	# 	new_item = Item.objects.first()
# 	# 	self.assertEqual(new_item.text ,'existing')
# 	# 	self.assertEqual(new_item.list , list_)

# 	def test_redirects_to_list_view(self):
# 		list_ = List.objects.create()
# 		wrong_list = List.objects.create()

# 		response = self.client.post('/lists/1/add_item',
#             data={'item_text': 'A new item for an existing list'}
#         )
# 		self.assertRedirects(response, '/lists/1/')

class NewItemTest(TestCase):

	def test_can_save_a_POST_request_to_an_existing_list(self):
		list_ = List.objects.create()
		wrong_list = List.objects.create()

		self.client.post(f'/lists/{list_.id}/save_to',data={'item_text': 'existing'})
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'existing')
		self.assertEqual(new_item.list, list_)


	def test_redirects_to_list_view(self):
		wrong_list = List.objects.create()
		list_ = List.objects.create()

		response = self.client.post(f'/lists/{list_.id}/save_to',data={'item_text': 'existing'})
		self.assertRedirects(response, f'/lists/{list_.id}/')

	def test_context_list(self):
		list_ = List.objects.create()
		wrong_list = List.objects.create()

		response = self.client.get(f'/lists/{list_.id}/')
		self.assertEqual(response.context['list'], list_)







class ListAndItemModelTest(TestCase):

	def test_model_save_retrieve(self):
		list_ = List()
		list_.save()

		# create item, set attribute text to a string and save it
		first_item = Item()
		first_item.text = "First"
		first_item.list = list_
		first_item.save()
		

		second_item = Item()
		second_item.text = "Second"
		second_item.list = list_
		second_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)

		# get all instances of Item
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]

		# test savedItem.text == createdItem.text
		self.assertEqual(first_item.text, first_saved_item.text)
		self.assertEqual(first_saved_item.list, list_)
		self.assertEqual(first_saved_item.list, list_)
		self.assertEqual(second_item.text, second_saved_item.text)

