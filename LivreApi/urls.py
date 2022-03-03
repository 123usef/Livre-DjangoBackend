from django import views
from django.urls import path
from . import views
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    #Login&Register
    path('api/register' , views.registration_view , name='register'),
    path('api/login', TokenObtainPairView.as_view(), name='login'),
    #Main_User_Profile
    path('api/profile/' , views.profile , name='profile'),
    path('api/manage_profile/' , views.manage_profile , name='manage_profile'),
    #Other_Users_Profile
    path('api/others_profile/<int:id>' , views.others_profile , name='others_profile'),
    #Messages
    path('api/messages/' , views.messages , name='messages'),
    path('api/message/<int:id>' , views.message , name='message'),
    #Books
    path('api/add_book/' , views.add_book , name='add_book'),
    path('api/exchange_book/<int:bookid>' , views.exchange_book , name='exchange_book'),
    path('api/accept_exchange/<int:exchangeid>' , views.accept_exchange , name='accept_exchange'),
    path('api/decline_exchange/<int:exchangeid>' , views.decline_exchange , name='decline_exchange'),

    #demo
    # path('api/books' , views.showbooks , name='books'),
    # path('api/books/<int:id>' , views.showbook , name='book'),

]