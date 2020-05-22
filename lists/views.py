from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List

def home_page(request):
    return render(request, 'base.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'display_list.html', {'items': items, 'list' : list_})


def save_item(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list = list_)
    return redirect(f'/lists/{list_.id}/')


def save_to(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')