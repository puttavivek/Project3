# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_item, name='add_item'),
    path('list/', views.list_items, name='list_items'),
    path('update/', views.update_item, name='update_item'),
    path('update/success/', views.update_item_success, name='update_item_success'),
    path('delete/', views.delete_item, name='delete_item'),
    path('delete/success/', views.delete_item_success, name='delete_item_success'),
    path('search/', views.search_item, name='search_item'),
    path('search/results/', views.search_results, name='search_results'),
    path('edit/', views.edit_item, name='edit_item'),
]
