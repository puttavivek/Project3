# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_item, name='add_item'),
    path('list/', views.list_items, name='list_items'),
    path('search/', views.search_item, name='search_item'),
    path('search/results/', views.search_results, name='search_results'),
    path('edit/', views.edit_item, name='edit_item'),
    path('print/', views.print_item, name='print_item'),
]
