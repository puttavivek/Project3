from django.db import models

class InventoryItem(models.Model):
    part_name = models.CharField(max_length=100, help_text='Enter the part name')
    part_no = models.CharField(max_length=50, unique=True, help_text='Enter the part number')
    model = models.CharField(max_length=50, help_text='Enter the model')
    stock_location = models.IntegerField(help_text='Enter the stock location')
    quantity = models.IntegerField(help_text='Enter the quantity')
    date_added = models.DateTimeField(auto_now_add=True, help_text='Date when the item was added')
