from pickle import GET
from unicodedata import category
from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import *
from .models import *


#Register_A_New_User
@api_view(['POST'])
def registration_view(request):
	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			user = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = user.email
			data['username'] = user.username
		else:
			data = serializer.errors
		return Response(data)

#View_(Logged in)Main_User_Profile
@api_view()
def profile(request):
    user = request.user
    main_user_serializer = MainUserSerializer(user, many=False)
    return Response(main_user_serializer.data)


#Edit_(Logged in)Main_User_Profile
@api_view(['POST'])
def manage_profile(request):
    user = request.user
    update_user = MainUserSerializer(data=request.data ,instance=user)
    if update_user.is_valid():
        update_user.save()
    return Response(update_user.data)


#View_Any_User_Profile
@api_view(['GET'])
def others_profile(request, id):
    user = User.objects.get(id = id)
    other_user_serializer = OtherUserSerializer(user, many=False)
    return Response(other_user_serializer.data)


#View_Main_User_Messages
@api_view(['GET'])
def messages(request):
    user = request.user
    messages = Message.objects.filter(m_receiver = user)
    all_my_messages = MessageSerializer(messages, many=True)
    return Response(all_my_messages.data)

#Sending_Messages
@api_view(['POST'])
def message(request, id):
    sender = request.user
    receiver = User.objects.get(id=id)
    message = Message.objects.create(m_receiver= receiver,m_sender=sender,content=request.data['content'])
    sent_message=MessageSerializer(message, many=False)
    return Response(sent_message.data)


#Add_Book
@api_view(['POST'])
def add_book(request):
    user = request.user
    data = request.data
    category = Category.objects.filter(name=data['cat']).first()
    book =Book.objects.create(title=data['title'],author=data['author'],description=data['description'],status=data['status'],user=user,cat=category)
    add_book = BookSerializer(book, many=False)
    return Response(add_book.data)

#View_Main_User_Book
@api_view(['GET'])
def show_main_user_books(request):
    user = request.user
    books = Book.objects.filter(user=user)
    user_books = BookSerializer(books , many=True)
    return Response(user_books.data)

#View_Main_User_Book
@api_view(['GET'])
def show_other_user_books(request, id):
    user = User.objects.get(id=id)
    books = Book.objects.filter(user=user)
    user_books = BookSerializer(books , many=True)
    return Response(user_books.data)


# Excahnge_Book
@api_view(['POST'])
def exchange_book (request,bookid):
    user = request.user
    book = Book.objects.get(id=bookid)
    transaction = Transaction.objects.create(book = book,tr_sender=user,tr_receiver=book.user)
    exchange_transaction = TransactionSerializer(transaction, many=False)
    return Response(exchange_transaction.data)


# Accept_Excahnging_Book
@api_view(['POST'])
def accept_exchange(request,exchangeid):
    user = request.user
    transaction = Transaction.objects.get(id = exchangeid)
    transaction.is_accepted=True
    transaction.save()    
    accept_transaction = TransactionSerializer(transaction, many=False)
    return Response(accept_transaction.data)


# Decline_Excahnging_Book
@api_view(['POST'])
def decline_exchange(request,exchangeid):
    user = request.user
    transaction = Transaction.objects.get(id = exchangeid)
    transaction.delete()
    return Response({"message":"transaction has been declined"})


#View_Main_User_Sent_Transactions
@api_view(['GET'])
def view_sender_transaction (request):
    user = request.user
    transaction = Transaction.objects.filter(tr_sender=user)
    view_sender_transaction = TransactionSerializer(transaction, many=True)
    return Response(view_sender_transaction.data)


#View_Main_User_Recived_Transactions
@api_view(['GET'])
def view_reciver_transaction (request):
    user = request.user
    transaction = Transaction.objects.filter(tr_receiver=user)
    view_reciver_transaction = TransactionSerializer(transaction, many=True)
    return Response(view_reciver_transaction.data)



# {
#  "username" : "nour2",
#  "email" : "nour@gmail.com",
#  "password":"nour12",
#  "password2" : "nour12",
#  "gender" : "male",
#  "date_of_birth" : "1999-07-12",
#  "location" : "cairo",
#  "phone" : "01272639811"
#  }

     


# Create your views here.


# @api_view()
# def showbooks(request):
#     books = Book.objects.all()
#     seri = BookSerializer(books , many=True)
#     return Response(seri.data)
   
# @api_view()
# def showbook(request ,id):
#     book = Book.objects.get(id=id)
#     seri = BookSerializer(book , many=False)
#     return Response(seri.data)

