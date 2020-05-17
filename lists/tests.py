# Here we'll start implementing unit tests, following the TDD cycle
# 1.  Write a FT which describes some well-defined behaviour from the user's pv
# 2. Make sure that FT fails as expected and move on to writing unit tests to define how we want our code which describes that functionally to behave. Each line of production code should be tested by at least one test
# 3. Once we have a failing UT, write the smallest amount of code which gets it to past. Iterate b/ 2-3 until the likelihood of the FT passing increases.
# 4. Rerun FT test, repeat 2-3 if failing. 

from django.test import TestCase
from django.urls import resolve
from lists.views import home_page 

class HomePageTest(TestCase):

    def test_home_resolver(self):
        # resolve() returns a ResolverMatch object if matched, func returns the function to be called
        # hence the test is defining the following API: GET http://localhost:<PORT#>/ <-> home_page() 
        found = resolve('/')
        self.assertEqual(found.func, home_page)

