from django import views
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('api/books' , views.showbooks , name='books'),
    path('api/books/<int:id>' , views.showbook , name='book'),

]