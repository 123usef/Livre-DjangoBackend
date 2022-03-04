from django import views
from django.urls import path
from . import views
from django.contrib import admin
# from rest_framework import routers #router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

# router = routers.SimpleRouter()

urlpatterns = [

    path('api/books' , views.showbooks , name='books'),
    path('api/books/<int:id>' , views.showbook , name='book'),
    # path('api/book/list' , views.BookListView , name='search'),
    path('api/register' , views.registration_view , name='register'),
    path('api/login', TokenObtainPairView.as_view(), name='login'),
    
    
    path('api/categorys', views.categorys_view, name='categorys'),
    path('api/category/<int:id>', views.category_view, name='category'),
    path('api/subscription/<int:id>', views.subscription_view, name='subscription'),
    
    path('api/unsubscription/<int:id>', views.unsubscription_view, name='unsubscription'),
    path('api/user_subscription/<int:id>', views.user_subscription_view, name='user_subscription'),
    path('api/add_book/' , views.add_book , name='add_book'),

    
]