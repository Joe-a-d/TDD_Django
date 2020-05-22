from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/shared')

    return render(request, 'base.html')


def view_list(request):
	items = Item.objects.all()
	return render(request, 'display_list.html', {'items': items})

