# views.py

from django.shortcuts import render, redirect
from .forms import AddItemForm
from .forms import SearchItemForm
from .forms import UpdateItemForm
from .forms import DeleteItemForm
from .forms import EditItemForm
from .models import Item
from .project1main import Web_Data as wd
from django.contrib import messages

def home(request):
    return render(request, 'inventory_app/home.html')

def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            # Process form data and add item to inventory
            part_name = form.cleaned_data['part_name']
            part_number = form.cleaned_data['part_number']
            model = form.cleaned_data['model']
            stock_location = form.cleaned_data['stock_location']
            quantity = form.cleaned_data['quantity']
            item_data = ["ADD", part_name, part_number, model, stock_location, quantity]
            returnstr = wd.web_data(item_data)
            print(returnstr)
            if returnstr == "Success":
                print("succ")
                messages.success(request, 'Item added successfully.')
            else:
                print("fail")
                messages.warning(request, 'Failed to add the data')
            Item.objects.create(part_name=part_name, part_number=part_number, model=model,
                                     stock_location=stock_location, quantity=quantity)
            #return redirect('home')  # Redirect to home page after successful addition
    else:
        form = AddItemForm()
    return render(request, 'inventory_app/add_item.html', {'form': form})

def edit_item(request):
    if request.method == 'POST':
        form = EditItemForm(request.POST)
        if form.is_valid():
            part_number = form.cleaned_data['part_number']
            quantity = form.cleaned_data['quantity']
            item_data = ["EDIT", part_number, quantity]
            returnstr = wd.web_data(item_data)
            print(returnstr)
            try:
                item_to_edit = Item.objects.get(part_number=part_number)
                item_to_edit.delete()
                return redirect('home')
            except Item.DoesNotExist:
                error_message = "Item with this part number does not exist."
                return render(request, 'inventory_app/remove_item.html', {'form': form, 'error_message': error_message})
    else:
        form = EditItemForm()
    return render(request, 'inventory_app/remove_item.html', {'form': form})

def list_items(request):
    items = Item.objects.all()
    return render(request, 'inventory_app/list_items.html', {'items': items})

def update_item(request):
    if request.method == 'POST':
        form = UpdateItemForm(request.POST)
        if form.is_valid():
            part_number = form.cleaned_data['part_number']
            quantity = form.cleaned_data['quantity']
            try:
                item = Item.objects.get(part_number=part_number)
                item.quantity += quantity
                item.save()
                return redirect('update_item_success')
            except Item.DoesNotExist:
                return render(request, 'inventory_app/update_item.html', {'form': form, 'error_message': 'Item with this part number does not exist.'})
    else:
        form = UpdateItemForm()
    return render(request, 'inventory_app/update_item.html', {'form': form})

def update_item_success(request):
    return render(request, 'inventory_app/update_item_success.html')

def delete_item_success(request):
    return render(request, 'inventory_app/delete_item_success.html')

def delete_item(request):
    if request.method == 'POST':
        form = DeleteItemForm(request.POST)
        if form.is_valid():
            part_number = form.cleaned_data['part_number']
            try:
                item = Item.objects.get(part_number=part_number)
                item.delete()
                return redirect('delete_item_success')
            except Item.DoesNotExist:
                return render(request, 'inventory_app/delete_item.html', {'form': form, 'error_message': 'Item with this part number does not exist.'})
    else:
        form = DeleteItemForm()
    return render(request, 'inventory_app/delete_item.html', {'form': form})

def search_item(request):
    if request.method == 'POST':
        form = SearchItemForm(request.POST)
        if form.is_valid():
            part_number = form.cleaned_data['part_number']
            items = Item.objects.filter(part_number=part_number)
            return render(request, 'inventory_app/search_result.html', {'items': items})
    else:
        form = SearchItemForm()
    return render(request, 'inventory_app/search_item.html', {'form': form})

def search_results(request):
    # Display search results functionality
    return render(request, 'inventory/search_results.html')

def delete_item_success(request):
    return render(request, 'inventory_app/delete_item_success.html')
