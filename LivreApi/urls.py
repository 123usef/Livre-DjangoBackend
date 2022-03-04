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
   
    
    #category
    path('api/categorys', views.categorys_view, name='categorys'),
    path('api/category/<int:id>', views.category_view, name='category'),
    path('api/subscription/<int:id>', views.subscription_view, name='subscription'),
    path('api/unsubscription/<int:id>', views.unsubscription_view, name='unsubscription'),
    path('api/user_subscription/<int:id>', views.user_subscription_view, name='user_subscription'),
    path('api/add_book/' , views.add_book , name='add_book'),

    
# Login & Register
    #Register_A_New_User
        path('api/register' , views.registration_view , name='register'),
    # Login  
        path('api/login', TokenObtainPairView.as_view(), name='login'),


############
# User Profile
    #Show_(Logged in)Main_User_Profile
        path('api/profile/' , views.profile , name='profile'),
    #Edit_(Logged in)Main_User_Profile
        path('api/manage_profile/' , views.manage_profile , name='manage_profile'),      
    #Show_Other_User_Profile
        path('api/others_profile/<int:id>' , views.others_profile , name='others_profile'),


############   
#Messages
    #View_Main_User_Messages
       path('api/messages/' , views.messages , name='messages'),
    #Sending_Message
        path('api/message/<int:id>' , views.message , name='message'),


############    
#Books
    #Add_Book
        path('api/add_book/' , views.add_book , name='add_book'),
    #Show_Main_User_Books
        path('api/show_main_user_books/' , views.show_main_user_books , name='show_main_user_books'),
    #Show_Other_User_Books
        path('api/show_other_user_books/<int:id>' , views.show_other_user_books , name='show_other_user_books'),


############    
#Transactions
    # Excahnge_Book
        path('api/exchange_book/<int:bookid>' , views.exchange_book , name='exchange_book'),
    # Accept_Excahnging_Book
        path('api/accept_exchange/<int:exchangeid>' , views.accept_exchange , name='accept_exchange'),
    # Decline_Excahnging_Book
        path('api/decline_exchange/<int:exchangeid>' , views.decline_exchange , name='decline_exchange'),
    
    #Show_Main_User_Sent_Transactions
        path('api/user_sender_transaction/' , views.show_sender_transaction , name='show_sender_transaction'),
    #Show_Main_User_Recived_Transactions
        path('api/user_reciver_transaction/' , views.show_reciver_transaction , name='show_reciver_transaction'),

    #demo
    # path('api/books' , views.showbooks , name='books'),
    # path('api/books/<int:id>' , views.showbook , name='book'),

]