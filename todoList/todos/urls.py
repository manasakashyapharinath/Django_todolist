from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index,  name='index'),
    path('add', views.addTodo, name='add'),
    path('complete', views.completeTodo, name='complete'),
    #path('', views.search,  name='search'),
    
]
