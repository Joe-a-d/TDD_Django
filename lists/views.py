from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	return HttpResponse("<html><h1> Test </h1></html>")
