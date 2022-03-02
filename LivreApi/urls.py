from django import views
from django.urls import path
from . import views
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/register' , views.register , name='register'),
    path('api/login' , obtain_auth_token , name='login'),

    path('api/books' , views.showbooks , name='books'),
    path('api/books/<int:id>' , views.showbook , name='book'),
]