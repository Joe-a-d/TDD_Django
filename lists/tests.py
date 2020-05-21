# Here we'll start implementing unit tests, following the TDD cycle
# 1.  Write a FT which describes some well-defined behaviour from the user's pv
# 2. Make sure that FT fails as expected and move on to writing unit tests to define how we want our code which describes that functionally to behave. Each line of production code should be tested by at least one test
# 3. Once we have a failing UT, write the smallest amount of code which gets it to past. Iterate b/ 2-3 until the likelihood of the FT passing increases.
# 4. Rerun FT test, repeat 2-3 if failing. 

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest, HttpResponse

from lists.views import home_page 
from lists.models import Item

class HomePageTest(TestCase):

    def test_home_template_used(self):
        # Test client is created for each test, which is accessed via the TestCase class, as oposed to client = Client() for each test

        response = self.client.get('/')

        self.assertTemplateUsed(response, 'base.html')


    def test_POST_save(self):
        response = self.client.post('/', data={'item_text': 'meditate for 20min'})


        # check that item has been saved
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        # check content of 'text'
        self.assertEqual(new_item.text, 'meditate for 20min')

        

    def test_POST_redirect(self):

        response = self.client.post('/', data={'item_text': 'meditate for 20min'})

        # check response for redirect
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')


    def test_save_only_onEnter(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_list_display_all(self):

        Item.objects.create(text="First")
        Item.objects.create(text="Second")

        response = self.client.get('/')

        self.assertIn("First", response.content.decode())
        self.assertIn("Second", response.content.decode())



class ItemModelTest(TestCase):

    def test_model_save_retrieve(self):
        # create item, set attribute text to a string and save it
        first_item = Item()
        first_item.text = "First"
        first_item.save()

        second_item = Item()
        second_item.text = "Second"
        second_item.save()

        # get all instances of Item
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        # test savedItem.text == createdItem.text
        self.assertEqual(first_item.text, first_saved_item.text)
        self.assertEqual(second_item.text, second_saved_item.text)