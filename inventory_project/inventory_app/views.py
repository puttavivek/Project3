# views.py

from django.shortcuts import render, redirect
from .forms import AddItemForm
from .forms import SearchItemForm
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
            if returnstr == "Success":
                messages.success(request, 'Item added successfully.')
            elif returnstr[0] == "Error":
                messages.warning(request, returnstr[1])
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
            print(returnstr[0])
            if returnstr[0] == "Success":
                print("inside success")
                messages.success(request, returnstr[1])
            elif returnstr[0] == "Error":
                messages.warning(request, returnstr[1])
    else:
        form = EditItemForm()
    return render(request, 'inventory_app/edit_item.html', {'form': form})

def search_item(request):
    if request.method == 'POST':
        form = SearchItemForm(request.POST)
        if form.is_valid():
            part_number = form.cleaned_data['part_number']
            item_data = ["SEARCH", part_number]
            returnstr = wd.web_data(item_data)
            return render(request, 'inventory_app/search_result.html', {'items': returnstr})
            #return render(request, 'inventory_app/search_result.html', {'items': items})
    else:
        form = SearchItemForm()
    return render(request, 'inventory_app/search_item.html', {'form': form})

def list_items(request):
    returnstr = wd.web_data(["BRING"])
    return render(request, 'inventory_app/list_items.html', {'items': returnstr})

def print_item(request):
    returnstr = wd.web_data(["PRINT"])
    if returnstr[0] == "Success":
        print("inside success")
        messages.success(request, returnstr[1])
    elif returnstr[0] == "Error":
        messages.warning(request, returnstr[1])

def search_results(request):
    # Display search results functionality
    return render(request, 'inventory/search_result.html')


