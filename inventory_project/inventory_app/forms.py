# inventory_app/forms.py

from django import forms


class AddItemForm(forms.Form):
    part_name = forms.CharField(max_length=100)
    part_number = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    stock_location = forms.IntegerField()
    quantity = forms.IntegerField()

class EditItemForm(forms.Form):
    part_number = forms.CharField(max_length=50)
    quantity = forms.IntegerField()

class SearchItemForm(forms.Form):
    part_number = forms.CharField(max_length=50)

class PrintListForm(forms.Form):
    pass