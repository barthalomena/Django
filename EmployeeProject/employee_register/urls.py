from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form,name=('employee_insert')),#get req, post info
    path('<int:id>/', views.employee_form,name=('employee_update')),#unpadte info
    path('delete/<int:id>/', views. employee_delete,name=('employee_deletes')),#delete info
    path('list/',views.employee_list,name=('employee_list'))#retrive & display
]