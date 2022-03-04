# from pickle import GET
# from unicodedata import category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import *
from .models import *
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics

# from django.contrib import messages
# from django.contrib import login,logout, authenticate

from rest_framework.authtoken.models import Token
# Create your views here.

#book
@api_view()
def showbooks(request):
    books = Book.objects.all()
    seri = bookserializer(books , many=True)
    return Response(seri.data)
   
@api_view()
def showbook(request ,id):
    book = Book.objects.get(id=id)
    seri = bookserializer(book , many=False)
    return Response(seri.data)

@api_view(['POST'])
def add_book(request):
    user = request.user
    data = request.data
    category = Category.objects.filter(name=data['cat']).first()
    book =Book.objects.create(title=data['title'],author=data['author'],description=data['description'],status=data['status'],user=user,cat=category)
    add_book = BookSerializer(book, many=False)
    return Response(add_book.data)

#registeration
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
#search and order
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = bookserializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['title', 'author']

    
#category 
#all category 
@api_view(['GET'])
def categorys_view(request):
    cat = Category.objects.all()
    categorys = CategorySerializer(cat, many =True)
    if request.user.is_authenticated:
        subsc = user.subscription_set.all()
    return Response(categorys.data)

#category page
@api_view()
def category_view(request ,id):
    cat = Category.objects.get(id=id)
    category = CategorySerializer(cat , many=False)
    return Response(category.data)

#subscription
@api_view(['GET'])
def user_subscription_view(request ,id):
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
    return  Response(subsc_seri.data)       
        
    

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
    subscribe = Subscription.objects.filter(user=request.user, cat=category).first()
    subscribe.delete()
    # unsubscribe_seri = UnSubscriptionSerializer(unsubscribe, many=False)
    return Response({"message":"you unsubscribed this category now"})

    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
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
