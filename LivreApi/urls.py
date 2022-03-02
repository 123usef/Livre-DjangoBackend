from django import views
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('api/books' , views.showbooks , name='books'),
    path('api/books/<int:id>' , views.showbook , name='book'),
    #main_user_profile
    path('api/profile/' , views.profile , name='profile'),
    path('api/manage_profile/' , views.manage_profile , name='manage_profile'),
    #user_profile
    path('api/others_profile/<int:id>' , views.others_profile , name='others_profile'),


]