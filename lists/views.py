from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	return render(request, "base.html", 
		{'list_item': request.POST.get('item_text', ''),})

