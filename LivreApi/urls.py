from django import views
from django.urls import path
from . import views
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
# Login & Register
    #Register_A_New_User
        path('api/register' , views.registration_view , name='register'),
    # Login  
        path('api/login', TokenObtainPairView.as_view(), name='login'),
############
# User Profile

    #View_(Logged in)Main_User_Profile
        path('api/profile/' , views.profile , name='profile'),
    #Edit_(Logged in)Main_User_Profile
        path('api/manage_profile/' , views.manage_profile , name='manage_profile'),      
    #Other_Users_Profile
        path('api/others_profile/<int:id>' , views.others_profile , name='others_profile'),

############   
#Messages
    #View_Main_User_Messages
    path('api/messages/' , views.messages , name='messages'),
    #Sending_Messages

    path('api/message/<int:id>' , views.message , name='message'),
    
    #Books
    path('api/add_book/' , views.add_book , name='add_book'),
    path('api/show_main_user_books/' , views.show_main_user_books , name='show_main_user_books'),
    path('api/show_other_user_books/<int:id>' , views.show_other_user_books , name='show_other_user_books'),

    path('api/exchange_book/<int:bookid>' , views.exchange_book , name='exchange_book'),

    path('api/accept_exchange/<int:exchangeid>' , views.accept_exchange , name='accept_exchange'),
    path('api/decline_exchange/<int:exchangeid>' , views.decline_exchange , name='decline_exchange'),
    
    #View_User_transaction
    path('api/user_sender_transaction/' , views.view_sender_transaction , name='view_sender_transaction'),
    path('api/user_reciver_transaction/' , views.view_reciver_transaction , name='view_reciver_transaction'),

    #demo
    # path('api/books' , views.showbooks , name='books'),
    # path('api/books/<int:id>' , views.showbook , name='book'),

]