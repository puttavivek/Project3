from django.db import models

class Item(models.Model):
    part_number = models.CharField(max_length=100, default='N/A')
    part_name = models.CharField(max_length=100, default='N/A')
    model = models.CharField(max_length=100, default='N/A')
    stock_location = models.CharField(max_length=100, default='N/A')
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.part_no
