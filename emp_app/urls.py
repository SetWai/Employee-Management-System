from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('all_emp', views.all_emp, name='all_emp'),
    path('get_departments/', views.get_departments, name='get_departments'),
    path('get_roles/', views.get_roles, name='get_roles'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('edit_emp', views.edit_emp, name='edit_emp'),
    path('edit_emp/<int:emp_id>', views.edit_emp, name='edit_emp'),
    path('remove_emp', views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
]