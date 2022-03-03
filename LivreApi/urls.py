from django import views
from django.urls import path
from . import views
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('api/books' , views.showbooks , name='books'),
    path('api/books/<int:id>' , views.showbook , name='book'),
    path('api/register' , views.registration_view , name='register'),
    path('api/login', TokenObtainPairView.as_view(), name='login'),
]