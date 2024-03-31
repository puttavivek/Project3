# inventory_app/forms.py

from django import forms
from .models import Item

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['part_name', 'part_number', 'model', 'stock_location', 'quantity']

class EditItemForm(forms.Form):
    part_number = forms.CharField(max_length=50)
    quantity = forms.IntegerField()

class SearchItemForm(forms.Form):
    part_number = forms.CharField(max_length=50)

class DeleteItemForm(forms.Form):
    part_number = forms.CharField(label='Part Number', max_length=100)

class SearchForm(forms.Form):
    part_number = forms.CharField(label='Part Number', max_length=100)

class UpdateItemForm(forms.Form):
    part_number = forms.CharField(label='Part Number', max_length=100)
    quantity = forms.IntegerField(label='Quantity')

class DeleteItemForm(forms.Form):
    part_number = forms.CharField(label='Part Number', max_length=100)