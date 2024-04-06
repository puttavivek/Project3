from django.shortcuts import render, redirect
from .forms import AddItemForm, SearchItemForm, EditItemForm, PrintListForm
from .project1main import Web_Data as wd
from django.contrib import messages

def home(request):
    """
    Render the home page.
    """
    return render(request, 'inventory_app/home.html')

def add_item(request):
    """
    Add an item to the inventory.
    """
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
            if returnstr[0] == "Success":
                messages.success(request, returnstr[1])
            elif returnstr[0] == "Error":
                messages.warning(request, returnstr[1])
    else:
        form = AddItemForm()
    return render(request, 'inventory_app/add_item.html', {'form': form})

def edit_item(request):
    """
    Edit an item in the inventory.
    """
    if request.method == 'POST':
        form = EditItemForm(request.POST)
        if form.is_valid():
            part_number = form.cleaned_data['part_number']
            quantity = form.cleaned_data['quantity']
            item_data = ["EDIT", part_number, quantity]
            returnstr = wd.web_data(item_data)
            if returnstr[0] == "Success":
                messages.success(request, returnstr[1])
            elif returnstr[0] == "Error":
                messages.warning(request, returnstr[1])
    else:
        form = EditItemForm()
    return render(request, 'inventory_app/edit_item.html', {'form': form})

def search_item(request):
    """
    Search for an item in the inventory.
    """
    if request.method == 'POST':
        form = SearchItemForm(request.POST)
        if form.is_valid():
            part_number = form.cleaned_data['part_number']
            item_data = ["SEARCH", part_number]
            returnstr = wd.web_data(item_data)
            if isinstance(returnstr, list):
                messages.warning(request, returnstr[1])
            else:
                return render(request, 'inventory_app/search_result.html', {'items': returnstr})
    else:
        form = SearchItemForm()
    return render(request, 'inventory_app/search_item.html', {'form': form})

def list_items(request):
    """
    List all items in the inventory.
    """
    returnstr = wd.web_data(["BRING"])
    return render(request, 'inventory_app/list_items.html', {'items': returnstr})

def print_item(request):
    """
    Print the list of items in the inventory.
    """
    if request.method == 'POST':
        form = PrintListForm(request.POST)
        if form.is_valid():
            returnstr = wd.web_data(["PRINT"])
            if isinstance(returnstr, list):
                messages.warning(request, returnstr[1])
            else:
                return returnstr
    else:
        form = PrintListForm()
    return render(request, 'inventory_app/print_list.html', {'form': form})

def search_results(request):
    """
    Display search results.
    """
    # This view might not be implemented yet or might be unnecessary.
    # Placeholder for future implementation.
    return render(request, 'inventory/search_result.html')
