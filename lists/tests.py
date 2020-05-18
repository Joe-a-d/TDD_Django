# Here we'll start implementing unit tests, following the TDD cycle
# 1.  Write a FT which describes some well-defined behaviour from the user's pv
# 2. Make sure that FT fails as expected and move on to writing unit tests to define how we want our code which describes that functionally to behave. Each line of production code should be tested by at least one test
# 3. Once we have a failing UT, write the smallest amount of code which gets it to past. Iterate b/ 2-3 until the likelihood of the FT passing increases.
# 4. Rerun FT test, repeat 2-3 if failing. 

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest, HttpResponse

from lists.views import home_page 


class HomePageTest(TestCase):

    def test_home_template_used(self):
        # Test client is created for each test, which is accessed via the TestCase class, as oposed to client = Client() for each test

        response = self.client.get('/')

        self.assertTemplateUsed(response, 'base.html')


;lsdk aslk dsa;ldkaks;ldk ;as;dlk a;lsk d;lka;sk d;lkas;lkd;alk; lkdl;ask d;lkas;l d;lask  aks dlaksjd jl ajsd lasd
a sdasdasd
asd
asd adas
d 
sa
 das 
 das dasd 
 as da asdasjdlajs ldkjasl kdjlajslk dlaksjd lkjaslkdj kajsdkjaskljd lajlkjdla jsd lkjal djlajs dljasl jda s
 