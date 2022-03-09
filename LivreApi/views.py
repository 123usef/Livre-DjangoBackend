from pickle import GET
from unicodedata import category
from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import *
from .models import *
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics

from rest_framework.authtoken.models import Token
# Create your views here.

# book
@api_view()
def showbooks(request):
    books = Book.objects.all()
    seri = BookSerializer(books, many=True)
    return Response(seri.data)

@api_view()
def showbook(request, id):
    book = Book.objects.get(id=id)
    seri = BookSerializer(book, many=False)
    return Response(seri.data)

# registeration
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

# category
# all category
@api_view(['GET'])
def categorys_view(request):
    cat = Category.objects.all()
    categorys = CategorySerializer(cat, many=True)
    if request.user.is_authenticated:
        subsc = User.subscription_set.all()
    return Response(categorys.data)

# category page
@api_view()
def category_view(request, id):
    cat = Category.objects.get(id=id)
    category = CategorySerializer(cat, many=False)
    return Response(category.data)

# subscription
@api_view(['GET'])
def user_subscription_view(request, id):
    cat = Category.objects.all()
    user = request.user
    subsc = user.Subscription_set.all()
    subsc_seri = UserSubscriptionSerializer(subsc, many=False, instance=user)
    subsc_id = []
    for subs in subsc:
        subsc_id.append(subs.cat_id)
    if len(subsc) == 0:
        books = Book.object.all()
    else:
        books = Book.object.filter(cat_id=subsc_id)
    return Response(subsc_seri.data)

@api_view(['GET'])
def subscription_view(request, id):
    category = Category.objects.get(id=id)
    # user_id = request.user.id
    subscribe = Subscription.objects.create(user=request.user, cat=category)
    subscribe_seri = SubscriptionSerializer(subscribe, many=False)
    return Response(subscribe_seri.data)

@api_view(['GET'])
def unsubscription_view(request, id):
    user = request.user
    category = Category.objects.get(id=id)
    subscribe = Subscription.objects.filter(
        user=request.user, cat=category).first()
    subscribe.delete()
    return Response({"message": "you unsubscribed this category now"})

# User Profile
# Show_(Logged in)Main_User_Profile
@api_view()
def profile(request):
    user = request.user
    main_user_serializer = MainUserSerializer(user, many=False)
    return Response(main_user_serializer.data)

# Edit_(Logged in)Main_User_Profile
@api_view(['POST'])
def manage_profile(request):
    user = request.user
    update_user = MainUserSerializer(data=request.data, instance=user)
    if update_user.is_valid():
        update_user.save()
    return Response(update_user.data)

# Show_Other_User_Profile
@api_view(['GET'])
def others_profile(request, id):
    user = User.objects.get(id=id)
    other_user_serializer = OtherUserSerializer(user, many=False)
    return Response(other_user_serializer.data)

# Messages
# View_Main_User_Messages
@api_view(['GET'])
def messages(request):
    user = request.user
    messages = Message.objects.filter(m_receiver=user)
    all_my_messages = MessageSerializer(messages, many=True)
    return Response(all_my_messages.data)

# Sending_Message
@api_view(['POST'])
def message(request, id):
    sender = request.user
    receiver = User.objects.get(id=id)
    message = Message.objects.create(
        m_receiver=receiver, m_sender=sender, content=request.data['content'])
    sent_message = MessageSerializer(message, many=False)
    return Response(sent_message.data)

# Books
# Add_Book
@api_view(['POST'])
def add_book(request):
    user = request.user
    data = request.data
    category = Category.objects.filter(name=data['cat']).first()
    book = Book.objects.create(title=data['title'], author=data['author'],
                               description=data['description'], status=data['status'], user=user, cat=category)
    add_book = BookSerializer(book, many=False)
    return Response(add_book.data)

# Show_Main_User_Books
@api_view(['GET'])
def show_main_user_books(request):
    user = request.user
    books = Book.objects.filter(user=user)
    user_books = BookSerializer(books, many=True)
    return Response(user_books.data)

# Show_Other_User_Books
@api_view(['GET'])
def show_other_user_books(request, id):
    user = User.objects.get(id=id)
    books = Book.objects.filter(user=user)
    user_books = BookSerializer(books, many=True)
    return Response(user_books.data)

# Transactions
# Excahnge_Book
@api_view(['POST'])
def exchange_book(request, bookid):
    user = request.user
    book = Book.objects.get(id=bookid)
    transaction = Transaction.objects.create(
        book=book, tr_sender=user, tr_receiver=book.user)
    exchange_transaction = TransactionSerializer(transaction, many=False)
    return Response(exchange_transaction.data)

# Accept_Excahnging_Book
@api_view(['POST'])
def accept_exchange(request, exchangeid):
    user = request.user
    transaction = Transaction.objects.get(id=exchangeid)
    transaction.is_accepted = True
    transaction.save()
    accept_transaction = TransactionSerializer(transaction, many=False)
    return Response(accept_transaction.data)

# Decline_Excahnging_Book
@api_view(['POST'])
def decline_exchange(request, exchangeid):
    user = request.user
    transaction = Transaction.objects.get(id=exchangeid)
    transaction.delete()
    return Response({"message": "transaction has been declined"})

# View_Main_User_Sent_Transactions
@api_view(['GET'])
def show_sender_transaction(request):
    user = request.user
    transaction = Transaction.objects.filter(tr_sender=user)
    show_sender_transaction = TransactionSerializer(transaction, many=True)
    return Response(show_sender_transaction.data)

# View_Main_User_Recived_Transactions
@api_view(['GET'])
def show_reciver_transaction(request):
    user = request.user
    transaction = Transaction.objects.filter(tr_receiver=user)
    show_reciver_transaction = TransactionSerializer(transaction, many=True)
    return Response(show_reciver_transaction.data)

#Rate
@api_view(['POST'])
def rate(request, id):
    sender = request.user
    receiver = User.objects.get(id=id)
    data = request.data
    rate=Rate.objects.create(rate = data['rate'] ,r_receiver = receiver ,r_sender=sender)
    rate_serializer = RateSerializer(rate, many=False)
    return Response(rate_serializer.data)

@api_view(['GET'])
def show_rate(request,id):
    user_get = User.objects.get(id=id)
    user_rate = Rate.objects.filter(r_receiver = user_get )
    total = 0
    sum=0
    for rate in user_rate:
        sum += float(rate.rate)  
    total = sum / len(user_rate)
    return Response(str(total))

#search and order
class Search(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, OrderingFilter]
    search_fields = ['title', 'author', 'status','description', 'cat__name', 'user__location']

# admin section starts from here
# --------------------------------
# listing operations ==> GET request
# ===================================
    # list users ==>user serializer ,
    # list books ==>books serializer ,
    # listing category ===category serializere

@api_view(['GET'])
def admin_listing(request, option):
    if option == 'list_users':
        users = User.objects.all()
        user_list = OtherUserSerializer(users, many=True)
        return Response(user_list.data)
    elif option == 'list_books':
        books = Book.objects.all()
        books_list = BookSerializer(books, many=True)
        return Response(books_list.data)
    elif option == 'list_category':
        cats = Category.objects.all()
        category_list = CategorySerializer(cats, many=True)
        return Response(category_list.data)
    else:
        return Response("wrong parameter")
# listing for admin ends
# add & delete operation for admin merged in one function
# category==> (add ,update,delete), book ==> delete book

@api_view(['POST', 'DELETE'])
def admin_operation(request, option, id=0):
    if request.method == 'POST':
        if option == 'add_category':
            data = request.data
            cat = Category.objects.create(name=data['name'])
            cat_ser = CategorySerializer(cat, many=False)
            return Response(cat_ser.data)
        elif option == 'edit_category':
            cat = Category.objects.get(id=id)
            cat_ser = CategorySerializer(data=request.data, instance=cat)
            if cat_ser.is_valid():
                cat_ser.save()
            return Response(cat_ser.data)
        elif option == "block_user":
            user = User.objects.get(id=id)
            user.is_blocked = 'True'
            user.save()
            return Response(user.is_blocked)
        elif option == "unblock_user":
            user = User.objects.get(id=id)
            user.is_blocked = 'False'
            user.save()
            return Response(user.is_blocked)
        else:
            return Response("wrong parameter")
    elif request.method == "DELETE":
        if option == "delete_category":
            cat = Category.objects.get(id=id)
            cat.delete()
            return Response("Category removed successfully ")
        elif option == "delete_book":
            boo = Book.objects.get(id=id)
            boo.delete()
            return Response("book deleted successfully")
        else:
            return Response("wrong parameter")

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
