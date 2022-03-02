from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import bookserializer , RegisterSerializer
from .models import *

# from django.contrib import messages
# from django.contrib import login,logout, authenticate

from rest_framework.authtoken.models import Token
# Create your views here.


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = "successfully register a new user."
        data['email'] = user.email
        data['username'] = user.username
        token = Token.objects.get(user=user).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data) 

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